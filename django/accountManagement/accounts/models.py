# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	mobile = models.IntegerField(max_length=10)
	email = models.CharField(max_length=250)

	def __str__(self):
		return self.first_name


