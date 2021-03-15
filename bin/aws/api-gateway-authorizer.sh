echo "AWS Account: $1"
# echo "cloudformation deploy --template-file dynamodb.yml --stack-name standard-manager-dynamodb --region sa-east-1 --profile tcc-td-puc-minas-admin"

# arn:aws:lambda:%s:%s:function:api-authorizer-stack-AuthRequest-1U7KVOWJVBOEM

aws apigatewayv2 create-authorizer \
    --api-id wcan6tfqua \
    --authorizer-type REQUEST \
    --identity-source '$request.header.Authorization' \
    --name api-authorizer-request \
    --authorizer-uri "arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:sa-east-1:$1:function:api-authorizer-stack-AuthRequest-1U7KVOWJVBOEM/invocations" \
    --authorizer-payload-format-version '2.0' \
    --enable-simple-responses \
    --profile tcc-td-puc-minas-admin

#aws apigatewayv2 create-authorizer \
#    --api-id wcan6tfqua \
#    --authorizer-type REQUEST \
#    --identity-source '$request.header.Authorization,$request.header.X-API-KEY' \
#    --name api-authorizer-request \
#    --authorizer-uri "arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:sa-east-1:$1:function:api-authorizer-stack-AuthRequest-1U7KVOWJVBOEM/invocations" \
#    --authorizer-payload-format-version '2.0' \
#    --enable-simple-responses \
#    --profile tcc-td-puc-minas-admin
#
#aws lambda add-permission \
#    --function-name my-authorizer-function \
#    --statement-id apigateway-invoke-permissions-abc123 \
#    --action lambda:InvokeFunction \
#    --principal apigateway.amazonaws.com \
#    --source-arn "arn:aws:execute-api:us-west-2:123456789012:api-id/authorizers/authorizer-id"
#
#aws apigatewayv2 update-route \
#    --api-id abcdef123 \
#    --route-id acd123 \
#    --authorization-type CUSTOM \
#    --authorizer-id def123