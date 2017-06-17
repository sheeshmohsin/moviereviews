# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from app.utils import get_upload_file_path
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
	added_by = models.ForeignKey(User, blank=True, null=True)
	name = models.CharField(max_length=150)
	description = models.TextField(blank=True, null=True)
	poster = models.ImageField(upload_to=get_upload_file_path, null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def avg_ratings_and_reviews_count(self):
		ratings = self.review_set.values_list('rating', flat=True)
		length = len(ratings)
		if length == 0:
			return 0, 0
		return reduce(lambda x, y: x + y, ratings) / (length * 1.0), length



class Review(models.Model):
	STATUS_CHOICES = (
		(1, _("*")),
		(2, _("**")),
		(3, _("***")),
		(4, _("****")),
		(5, _("*****"))
	)
	added_by = models.ForeignKey(User)
	movie = models.ForeignKey(Movie)
	rating = models.IntegerField(choices=STATUS_CHOICES, default=1)
	review = models.TextField()

	def __str__(self):
		return self.review
