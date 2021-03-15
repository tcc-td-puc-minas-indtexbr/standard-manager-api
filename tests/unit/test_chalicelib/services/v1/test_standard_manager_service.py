import unittest

from unittest_data_provider import data_provider

from chalicelib.config import get_config
from chalicelib.http_resources.request import ApiRequest
from chalicelib.logging import get_logger
from chalicelib.services.v1.standard_manager_service import StandardManagerService
from tests import ROOT_DIR
from tests.functional.functionaltestutils import BaseFunctionalTestCase
from tests.functional.helpers.connection_helper import ConnectionHelper, DynamoDBHelper
from tests.unit.mocks.boto3_mocks import table_mock
from tests.unit.mocks.nosql_database_mock import get_connection
from tests.unit.testutils import get_function_name, BaseUnitTestCase


def get_request():
    request = ApiRequest()
    request.limit = 2

    request2 = ApiRequest()
    request2.limit = 2
    request2.offset = 1

    return (request,), (request2,),


class StandardManagerServiceTestCase(BaseUnitTestCase):

    def setUp(self):
        super().setUp()
        # sobrescreve o mock
        self.connection = get_connection()
        self.config = get_config()

        data = {
            'Items': [
                {'comite': 'ABNT', 'language': 'Português', 'title': 'ISO 5000',
             'uuid': '3fa85f64-5717-4562-b3fc-2c963f66afa6', 'url': '', 'objective': '',
             'identification': 'ISO 5000:2000', 'pages': 10, 'file': '', 'price': '10.00',
             'validity_start': '2021-01-18', 'title_global_language': 'ISO 5000', 'organization': 'ABNT',
             'publication_date': '2021-01-18', 'currency': 'Real', 'status': 'Em Vigor'},
                {'comite': '', 'language': 'English', 'title': 'Sistemas de gestão da qualidade - Requisitos',
             'uuid': '067d914c-cb19-4f3f-8755-584e0eafe344',
             'url': 'http://paginapessoal.utfpr.edu.br/canabarro/iso%209000-2015.pdf/at_download/file',
             'objective': None, 'identification': 'ISO 9001:2015', 'pages': 30,
             'file': 'NORMA%20ISO%2090002015.pdf', 'price': '170.00', 'validity_start': '2015-10-30',
             'title_global_language': '', 'organization': 'ABNT - Associação Brasileira de Normas Técnicas',
             'publication_date': '2015-09-30', 'currency': 'BRL', 'status': 'Arquivado'}],
            'Count': 2,
            'ScannedCount': 2,
            'ResponseMetadata': {'RequestId': 'ebe11a2f-1b8f-472b-8507-c9aadeb3a379', 'HTTPStatusCode': 200,
                                 'HTTPHeaders': {'date': 'Sun, 28 Feb 2021 03:06:49 GMT',
                                                 'content-type': 'application/x-amz-json-1.0',
                                                 'x-amz-crc32': '2132082689',
                                                 'x-amzn-requestid': 'ebe11a2f-1b8f-472b-8507-c9aadeb3a379',
                                                 'content-length': '1130', 'server': 'Jetty(9.4.18.v20190429)'},
                                 'RetryAttempts': 0}}
        # Mock returns
        table_mock.scan.side_effect = lambda: data
        table_mock.item_count = data['Count']

    @data_provider(get_request)
    def test_list(self, request):
        self.logger.info('Running test: %s', get_function_name(__name__))
        service = StandardManagerService(logger=self.logger, config=self.config, connection=self.connection)
        data = service.list(request)
        self.assertIsNotNone(data)
        # self.assertTrue(len(data) == request.limit)

    @data_provider(get_request)
    def test_count(self, request):
        """

        :param (ApiRequest) request:
        :return:
        """
        self.logger.info('Running test: %s', get_function_name(__name__))
        service = StandardManagerService(logger=self.logger, config=self.config, connection=self.connection)
        data = service.count(request)

        self.assertIsNotNone(data)
        self.assertTrue(data > 0)


if __name__ == '__main__':
    unittest.main()
