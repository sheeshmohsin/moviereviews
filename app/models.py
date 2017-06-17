# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app.utils import get_upload_file_path
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db.models import Q

# Create your models here.
class Movie(models.Model):
    added_by = models.ForeignKey(User)
    name = models.CharField(max_length=150)
    description = models.TextField()
    poster = models.ImageField(upload_to=get_upload_file_path)

    def __str__(self):
        return self.name

    @property
    def avg_ratings(self):
        ratings = self.review_set.values_list('rating', flat=True)
        length = len(ratings)
        if length == 0:
            return False
        return round(reduce(lambda x, y: x + y, ratings) / (length * 1.0), 2)

    @property
    def reviews_count(self):
        return self.review_set.filter(~Q(review='')).count()


class Review(models.Model):
    STATUS_CHOICES = (
        (1, _("*")),
        (2, _("**")),
        (3, _("***")),
        (4, _("****")),
        (5, _("*****"))
    )
    added_by = models.ForeignKey(User, blank=True, null=True)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField(choices=STATUS_CHOICES)
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.review
