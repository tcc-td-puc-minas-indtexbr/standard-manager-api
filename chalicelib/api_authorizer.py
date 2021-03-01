from chalice.app import Authorizer


class ApiRequestAuthorizer(Authorizer):

    _AUTH_TYPE = 'custom'

    def __init__(self, name, authorizer_uri, ttl_seconds=300,identity_source=None):

        if not identity_source:
            identity_source = ['X-API-KEY', 'Authorization']

        self.name = name
        self._authorizer_uri = authorizer_uri
        self._identity_source = ['method.request.header.%s' % ids for ids in identity_source]
        self._ttl_seconds = ttl_seconds



    def to_swagger(self):
        """
        https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions-authorizer.html#api-gateway-swagger-extensions-authorizer-example
        :return:
        """
        return {
            'type': 'apiKey',
            'name': 'Unused',
            'in': 'header',
            'x-amazon-apigateway-authtype': self._AUTH_TYPE,
            'x-amazon-apigateway-authorizer': {
                'type': 'request',
                'identitySource': ','.join(self._identity_source),
                # "authorizerCredentials": "arn:aws:iam::123456789012:role/AWSepIntegTest-CS-LambdaRole",
                'authorizerUri': self._authorizer_uri,
                'authorizerResultTtlInSeconds': self._ttl_seconds
            }
        }