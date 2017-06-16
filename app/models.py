# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Movie(models.Model):
	added_by = models.ForeignKey(User)
	name = models.CharField(max_length=150)
	description = models.TextField()

	def __str__(self):
		return self.name


class Reviews(models.Model):
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
		return self.rating
