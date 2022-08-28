from django.db.models import Count
from django.db.models.query import QuerySet
from django.db import models


class ConnectionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("user1", "user2").all()

    def user_connections(self, _id):
        return self.select_related("user1", "user2").filter(user1__id=id)

