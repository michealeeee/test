from django.apps import AppConfig
from mongoengine import connect


class TestAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_app'

    def ready(self):
            connect(db = 'test',
                    host='mongodb+srv://mke00007_db_user:ofLjBkXKyzGZgYKJ@testprojectdb.vs6rvei.mongodb.net/?appName=test',)
            