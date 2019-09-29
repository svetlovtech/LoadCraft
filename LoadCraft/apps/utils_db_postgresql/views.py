from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework import viewsets
from .serializers import PostgresqlSettingsSerializer
from .models import PostgresqlSettings


class PostgresqlSettingsView(viewsets.ModelViewSet):
    queryset = PostgresqlSettings.objects.all().order_by('label_id')
    serializer_class = PostgresqlSettingsSerializer


def check_connection(request, postgresql_settings_label_id):
    postgresql_settings = PostgresqlSettings.objects.get(
        label_id=postgresql_settings_label_id)
    return HttpResponse(postgresql_settings)


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
