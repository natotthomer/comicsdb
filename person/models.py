from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=256, blank=True, null=True)
    surname = models.CharField(max_length=16, blank=True, null=True)
