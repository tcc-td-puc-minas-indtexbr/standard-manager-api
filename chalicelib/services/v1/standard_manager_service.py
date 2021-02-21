from chalicelib.config import get_config
from chalicelib.database import get_connection
from chalicelib.logging import get_logger
from chalicelib.nosql.repositories.v1.standard import StandardRepository


class StandardManagerService:
    DEBUG = False
    ENTITY = None
    REPOSITORY = StandardRepository
    VALIDATOR = None

    def __init__(self, logger=None, config=None, connection=None):
        # logger
        self.logger = logger if logger is not None else get_logger()
        # configurations
        self.config = config if config is not None else get_config()
        # database connection
        self.connection = connection if connection is not None else get_connection()

        if self.DEBUG:
            self._repository = self.REPOSITORY(self.connection, self.config.DYNAMODB_TABLE_NAME, logger)
        else:
            self._repository = self.REPOSITORY(self.connection, self.config.DYNAMODB_TABLE_NAME)

    def get(self):
        pass

    def list(self, api_request):

        request = self.validate_request(api_request)

        data = self._repository.list(where=request['where'], offset=request['offset'],
                                     limit=request['limit'], fields=request['fields'],
                                     sort_by=request['sort_by'], order_by=request['order_by'])
        return data

    def count(self, api_request):

        request = self.validate_request(api_request)

        data = self._repository.count(where=request['where'], sort_by=request['sort_by'], order_by=request['order_by'])

        count = 0
        try:
            count = data.get('total')
        except Exception as err:
            self.logger.error(err)

        return count

    def create(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def validate_request(self, api_request):
        # TODO implementar quando necessario
        return api_request
