from django.db import models


class PostgresqlSettings(models.Model):
    label_id = models.CharField(max_length=30, primary_key=True)
    dbname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    host = models.CharField(max_length=150)
    port = models.IntegerField()

    def __str__(self):
        return f'{self.label_id} dbname:{self.dbname} username:{self.username}'
