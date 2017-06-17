# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import Movie, Review

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
