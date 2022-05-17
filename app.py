import json
import os
from datetime import datetime

import SensiCommon as SC
import mailchimp_transactional as MailchimpTransactional
import rollbar as rollbar
from SensiCommon.db.customers_model import CareLog, Device, DashboardUsersToCustomer, DashboardUser, Customer
from exponent_server_sdk import (
    DeviceNotRegisteredError,
    PushClient,
    PushMessage,
    PushServerError,
    PushTicketError,
)
from mailchimp_transactional.api_client import ApiClientError
from requests.exceptions import ConnectionError, HTTPError
from retry import retry
from twilio.rest import Client
from template import real_time_email_template_body, real_time_email_template_head
import sentry_sdk
from loguru import logger
from sensi_logger.log import initialize


initialize(enable_stackprinter_stacktrace=True, log_level="INFO",
           service_name="realtime-alerts")

sentry_sdk.init(
    dsn=os.environ.get("sentry_dsn", ""),
    environment=os.environ.get("env_name", "dev"),
    traces_sample_rate=float(os.environ.get("sentry_trace", "0.0"))
)

ssm_params = SC.cloud.ssm.get_SSM_params()
for key, value in ssm_params.items():
    os.environ[key] = str(value)

account_sid = os.environ.get('SMS_ACCOUNT_SID')
auth_token = os.environ.get('SMS_AUTH_TOKEN')
from_number = os.environ.get('SMS_FROM_NUMBER')
mailchimp_api_key = os.environ.get('MAILCHIMP_API_KEY')

client = Client(account_sid, auth_token)

subject = 'High Level alert from Sensi.ai'
MESSAGE = '{} - Sending a {} to {} , {}'


def send_sms(to, message):
    message = client.messages \
        .create(
        body=message,
        from_=from_number,
        to=to
    )

    logger.info(message.sid)


def send_email_mailchimp(to, subject, html):
    email = {
        "from_email": "info@sensi.ai",
        "from_name": "Sensi.Ai",
        "to": [{"email": to, "type": "cc"}],
        "html": html,
        "subject": subject,
        "track_opens": True,
        "track_clicks": True,
    }

    try:
        # send to mailchimp endpoint
        mailchimp = MailchimpTransactional.Client(mailchimp_api_key)
        response = mailchimp.messages.send({"message": email})
        logger.info(response)
    except ApiClientError as error:
        logger.info("An exception occurred: {}".format(error.text))
    except Exception as err:
        logger.info(f'Error: %s' % str(err))
    finally:
        logger.info(f'Email Sent To %s' % email)


def generate_link(department, site, customer):
    return f"Department {department}" if customer.has_departments else site


def lambda_handler(event, context):
    # for record in event['Records']:
    logger.info("event ---- %s " % str(event))
    payload = event['Records'][0]['body']
    # payload = record['body']
    logger.info(payload)
    id = json.loads(payload)['care_log_id']
    logger.info('this is the cl id {}'.format(id))

    with SC.db.PostgresSessionMaker() as session_src:
        cl = session_src.query(CareLog).filter(CareLog.id == id).first()
        device = session_src.query(Device).filter(Device.id == cl.device_id).first()
        customer = session_src.query(Customer).filter(Customer.id == device.customer_id).first()
        customer_name = customer.name if customer and customer.name else ''

        dashboardUsersToCustomer = session_src.query(DashboardUsersToCustomer).filter(
            device.customer_id == DashboardUsersToCustomer.customer_id,
            device.site == DashboardUsersToCustomer.site,
            device.department == DashboardUsersToCustomer.department).all()

        for duc in dashboardUsersToCustomer:
            try:
                user = session_src.query(DashboardUser).filter(DashboardUser.id == duc.dashboard_user_id).first()
                if user and 'real_time' in user.configuration:
                    try:
                        if is_valid_email_config(user):
                            formatted_html = real_time_email_template_head + real_time_email_template_body.format(
                                unit=device.unit,
                                time=datetime.strftime(cl.ts, '%m-%d-%Y %H:%M %p'),
                                labels=cl.labels
                            )
                            send_email_mailchimp(user.email, subject, formatted_html)
                            logger.info(MESSAGE.format('Success', 'email', str(user.username), ''))
                    except Exception as e:
                        logger.info(MESSAGE.format('Failed', 'email', str(user.username), str(e)))
                    try:
                        if is_valid_sms_config(user):
                            send_sms(user.contact_number,
                                     f' A high level alert of {cl.labels} from Sensi.AI was detected in the following home: {device.unit}.\nplease login to https://app.sensi.ai')
                            logger.info(MESSAGE.format('Success', 'SMS', str(user.username), ''))
                    except Exception as e:
                        logger.info(MESSAGE.format('Failed', 'SMS', str(user.username), str(e)))
                    try:
                        if is_valid_mobile_push_config(user):
                            send_push_message(user.configuration['push_notifications_token'],
                                              "New real time alert in care log. Tap here to review the event",
                                              get_push_notifications_data(care_log_id=cl.id,
                                                                          customer_name=customer_name, site=device.site,
                                                                          department=device.department,
                                                                          link_name=generate_link(
                                                                              department=duc.department,
                                                                              site=duc.site,
                                                                              customer=customer)))
                            logger.info(MESSAGE.format('Success', 'push', str(user.username), ''))
                    except Exception as e:
                        logger.info(MESSAGE.format('Failed', 'mobile push', str(user.username), str(e)))
            except Exception as e:
                logger.info(MESSAGE.format('Failed', 'process', str(user.username), str(e)))

            # session_src.close()
            print('finished')


def is_valid_mobile_push_config(user):
    return 'push_notifications_token' in user.configuration and 'mobile_push_notifications' in \
           user.configuration['real_time'] and user.configuration['real_time'][
               'mobile_push_notifications'] and len(user.configuration['push_notifications_token']) > 0


def is_valid_sms_config(user):
    return 'sms' in user.configuration['real_time'] and user.configuration['real_time'][
        'sms'] and user.contact_number and len(
        user.contact_number) > 0


def is_valid_email_config(user):
    return 'email' in user.configuration['real_time'] and user.configuration['real_time']['email'] and len(
        user.email) > 0


def is_eligible_contact_number(customer, site):
    return customer.configuration and 'contact_number' in customer.configuration and len(
        customer.configuration['contact_number']) and len(customer.configuration['contact_number'][site]) > 0


def send_push_message(token, message, extra=None):
    try:
        response = PushClient().publish(
            PushMessage(to=token,
                        body=message,
                        data=extra))
    except PushServerError as exc:
        # Encountered some likely formatting/validation error.
        rollbar.report_exc_info(
            extra_data={
                'token': token,
                'message': message,
                'extra': extra,
                'errors': exc.errors,
                'response_data': exc.response_data,
            })
        raise
    except (ConnectionError, HTTPError) as exc:
        # Encountered some Connection or HTTP error - retry a few times in
        # case it is transient.
        rollbar.report_exc_info(
            extra_data={'token': token, 'message': message, 'extra': extra})
        raise retry(exc=exc)

    try:
        # We got a response back, but we don't know whether it's an error yet.
        # This call raises errors so we can handle them with normal exception
        # flows.
        response.validate_response()
    except DeviceNotRegisteredError:
        # Mark the push token as inactive
        from notifications.models import PushToken
        PushToken.objects.filter(token=token).update(active=False)
    except PushTicketError as exc:
        # Encountered some other per-notification error.
        rollbar.report_exc_info(
            extra_data={
                'token': token,
                'message': message,
                'extra': extra,
                'push_response': exc.push_response._asdict(),
            })
        raise retry(exc=exc)


def get_push_notifications_data(care_log_id: int, customer_name: str, site: str, department: str, link_name: str):
    return json.dumps({
        "care_log_id": care_log_id,
        "customer_name": customer_name,
        "site": site,
        "department": department,
        "link_name": link_name
    })


if __name__ == '__main__':
    pass
    # print(get_push_notifications_data(1234,1,"site","department"))
    # events = {'Records': [{'body': '{"care_log_id": 48595457}'}]}
    # lambda_handler(events, None)
    #
