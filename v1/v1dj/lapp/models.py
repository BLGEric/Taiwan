from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Logindb(models.Model):
	username = models.CharField(max_length=30)
	account = models.CharField(max_length=30)
	password = models.CharField(max_length=50)
	def __str__(self):
		return self.username