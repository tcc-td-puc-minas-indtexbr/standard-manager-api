echo "AWS Account: $1"
echo "docker tag sigo-frontend:latest $1.dkr.ecr.sa-east-1.amazonaws.com/sigo-frontend:latest"
docker tag sigo-frontend:latest $1.dkr.ecr.sa-east-1.amazonaws.com/sigo-frontend:latest