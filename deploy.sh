docker build -f Dockerfile -t 443793523615.dkr.ecr.eu-west-1.amazonaws.com/realtime-alerts:1.1 --progress=plain .
#docker run -t insert_full_segment_to_filter:1.14
aws ecr get-login-password --profile=produser --region eu-west-1 | docker login --username AWS --password-stdin 443793523615.dkr.ecr.eu-west-1.amazonaws.com
#aws ecr create-repository --profile produser --repository-name realtime-alerts --image-scanning-configuration scanOnPush=true --region eu-west-1
#docker tag realtime-alerts:1.1 443793523615.dkr.ecr.eu-west-1.amazonaws.com/realtime-alerts:1.1

docker push 443793523615.dkr.ecr.eu-west-1.amazonaws.com/realtime-alerts:1.1


#docker build -f weekly.Dockerfile -t 567871189482.dkr.ecr.eu-central-1.amazonaws.com/insert-full-segment .
##docker run -t filter:generate_params_lambda_1.0
#aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 567871189482.dkr.ecr.eu-central-1.amazonaws.com
##docker tag device-status-check 567871189482.dkr.ecr.eu-central-1.amazonaws.com/device-status-check
#docker push 567871189482.dkr.ecr.eu-central-1.amazonaws.com/insert-full-segment