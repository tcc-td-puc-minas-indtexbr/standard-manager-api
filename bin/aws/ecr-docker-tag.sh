echo "AWS Account: $1"
echo "docker tag standard-manager-api:latest $1.dkr.ecr.sa-east-1.amazonaws.com/standard-manager-api:latest"
docker tag standard-manager-api:latest $1.dkr.ecr.sa-east-1.amazonaws.com/standard-manager-api:latest