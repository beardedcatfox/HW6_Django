from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=119)
    last_name = models.CharField(max_length=119)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Log(models.Model):
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(default=dict)

    def __str__(self):
        return self.path
