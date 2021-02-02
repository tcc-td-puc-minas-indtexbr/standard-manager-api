terraform plan -var "account_id=$1" -out $2.binary
terraform show -json $2.binary > $2
