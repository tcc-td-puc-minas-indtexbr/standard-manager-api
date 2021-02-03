echo "AWS Account: $1"
echo "docker push $1.dkr.ecr.sa-east-1.amazonaws.com/sigo-frontend:latest"
docker push $1.dkr.ecr.sa-east-1.amazonaws.com/sigo-frontend:latest