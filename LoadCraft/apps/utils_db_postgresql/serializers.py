from rest_framework import serializers
from .models import PostgresqlSettings


class PostgresqlSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostgresqlSettings
        fields = ('label_id', 'dbname', 'username', 'password', 'host', 'port')
