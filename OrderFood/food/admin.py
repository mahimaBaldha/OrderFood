# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import order, items

# Register your models here.

admin.site.register(order)
admin.site.register(items)