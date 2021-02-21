class StandardRepository:
    def __init__(self, connection, table_name, logger=None):
        """
        :param (pytrine.dbal.connection.Connection) connection:
        """

        self._connection = connection
        self._logger = logger
        self.table_name = table_name
        self._table = self._connection.Table(self.table_name)

    def list(self, where, offset=None, limit=None, fields=None, sort_by=None, order_by=None):
        scan_params = {}
        #     filter_expression = None
        #     if startswith is not None:
        #         filter_expression = self._add_to_filter_expression(
        #             filter_expression, Attr('name').begins_with(startswith)
        #         )
        #     if media_type is not None:
        #         filter_expression = self._add_to_filter_expression(
        #             filter_expression, Attr('type').eq(media_type)
        #         )
        #     if label is not None:
        #         filter_expression = self._add_to_filter_expression(
        #             filter_expression, Attr('labels').contains(label)
        #         )
        #     if filter_expression:
        #         scan_params['FilterExpression'] = filter_expression
        response = self._table.scan(**scan_params)

        return response['Items']

    def count(self, where, sort_by, order_by):
        # Todo ver com filtros
        # print
        # dynamodb_table.query_count(
        #     index='first_name-last_name-index',  # Get indexes from indexes tab in dynamodb console
        #     first_name__eq='John',  # add __eq to your index name for specific search
        #     last_name__eq='Smith'  # This is your range key
        # )
        return {"total": self._table.item_count}
