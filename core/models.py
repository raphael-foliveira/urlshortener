from django.db import models


class Link(models.Model):
    id = models.AutoField(primary_key=True)
    original_url = models.URLField(max_length=2000)
    short_url = models.CharField(max_length=100, unique=True)
