from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action, api_view, schema
from rest_framework.schemas import AutoSchema
from rest_framework import viewsets

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import PostgresqlSettingsSerializer
from .models import PostgresqlSettings

import psycopg2
import logging
import json

logger = logging.getLogger(__name__)


class PostgresqlSettingsView(viewsets.ModelViewSet):
    """This API allows you to interact, add, delete PostgreSQL configurations."""
    queryset = PostgresqlSettings.objects.all().order_by('label_id')
    serializer_class = PostgresqlSettingsSerializer

    @swagger_auto_schema(methods=['get'], responses={204: 'Database connection checked complited', 504: 'Database connection checked failed'})
    @action(methods=['GET'], detail=True)
    def check_connection(self, request, pk: PostgresqlSettings):
        """"This method allows you to check the connection to the database."""
        logging.info(
            f'Checking database {pk} connection started...')

        response = None
        try:
            postgresql_setting: PostgresqlSettings = PostgresqlSettings.objects.get(
                pk=pk)
            logging.info(
                f'postgresql_setting{type(postgresql_setting)} = {postgresql_setting}')
            connection: psycopg2.extensions.connection = psycopg2.connect(user=postgresql_setting.username,
                                                                          password=postgresql_setting.password,
                                                                          host=postgresql_setting.host,
                                                                          port=postgresql_setting.port,
                                                                          database=postgresql_setting.dbname)

            logging.info(f'connection{type(connection)} = {connection}')
            database_info: dict = connection.get_dsn_parameters()
            cursor = connection.cursor()
            cursor.execute("SELECT version();")
            database_info['database_info'] = str(cursor.fetchone()).strip('[]')
            logging.info(f'database_info = {database_info}')

            response = HttpResponse(json.dumps(database_info),
                                    content_type="application/json; charset=utf-8")
            response.status_code = 200
        except (Exception, psycopg2.Error) as error:
            error_message = f'Error while connecting to PostgreSQL: {error}'
            response = HttpResponse(error_message)
            response.status_code = 503
            logging.error(error_message)
        finally:
            try:
                if(connection):
                    cursor.close()
                    connection.close()
            except (UnboundLocalError) as error:
                logging.warning('Database connection already closed')
            logging.info(
                f'Checking database {pk} connection completed')
            return response


# @api_view(['get', 'post'])
# def check_connection(request, postgresql_settings_label_id):
#     postgresql_settings = PostgresqlSettings.objects.get(
#         label_id=postgresql_settings_label_id)
#     return HttpResponse(postgresql_settings)


def get_query_by_id(request):
    return HttpResponse('')


def pg_stat_statements_reset(request):
    return HttpResponse('')


def pg_stat_statements_collect_json_format(request):
    return HttpResponse('')


def pg_stat_activity_collect_json_format(request):
    return HttpResponse('')


def run_custom_query(request):
    return HttpResponse('')


# test_param1 = openapi.Parameter(
#     in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN, name='test1', description="test manual param", )
# test_param2 = openapi.Parameter(
#     in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, name='test2', description="test manual param", enum=['qwerty', 'asdfgh', 'cxvb'])
# test_param3 = openapi.Parameter(
#     in_=openapi.IN_QUERY, type=openapi.TYPE_NUMBER, name='test3', description="test manual param", )
# test_param3 = openapi.Parameter(
#     in_=openapi.IN_PATH,  type=openapi.TYPE_NUMBER, name='test4', description="test manual param", )
# @swagger_auto_schema(manual_parameters=[test_param1, test_param2, test_param3], methods=['put', 'post'], responses={404: 'slug not found'})
# @api_view(['put', 'post'])
# def cancel_payments(request, postgresql_settings_label_id: str, pk: int):
#     """
#     Returns a list of all **active** accounts in the system.

#     For more details on how accounts are activated please [see here][ref].

#     [ref]: http://example.com/activating-accounts
#     """
#     logging.info('cancel_payments started...')

#     var_name = 'qweasdasdsad'
#     logging.info(f'var_name{type(var_name)} = {var_name}')

#     logging.info('cancel_payments completed')
#     return Response('{Payment canceled!}')
