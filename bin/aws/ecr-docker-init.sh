echo "AWS Account: $1"
echo "aws ecr get-login-password --region sa-east-1 --profile tcc-td-puc-minas-admin| docker login --username AWS --password-stdin $1.dkr.ecr.sa-east-1.amazonaws.com"
aws ecr get-login-password --region sa-east-1 --profile tcc-td-puc-minas-admin | docker login --username AWS --password-stdin $1.dkr.ecr.sa-east-1.amazonaws.com