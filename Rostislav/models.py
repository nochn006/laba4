from django.db import models


class Films(models.Model):
    name = models.CharField(max_length=30)


class Category(models.Model):
    name = models.CharField(max_length=30)

