# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    isbn = models.CharField(max_length=16, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)