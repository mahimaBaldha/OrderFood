# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class items(models.Model):
    ord_id = models.TextField(null=False)
    ord_price = models.PositiveIntegerField(default=0)
    ord_address = models.TextField()


class order(models.Model):
    # id = models.PositiveIntegerField(default=0)
    name = models.TextField(null=False)
    img = models.TextField()
    price = models.PositiveIntegerField(default=0)
