FROM python:3.8-slim

WORKDIR /usr/src/app

RUN apt-get update -y
RUN apt-get install git libsndfile1 libsndfile1-dev -y
RUN apt-get install ffmpeg -y
RUN pip install awslambdaric

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "-m", "awslambdaric" ]
CMD [ "app.lambda_handler" ]
