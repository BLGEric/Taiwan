from django.db import models

class Logindb(models.Model):
	username = models.CharField(max_length=30)
	account = models.CharField(max_length=30)
	password = models.CharField(max_length=50)
	def __str__(self):
		return self.username


class Newinfo(models.Model):
	title = models.CharField(max_length=30)
	intro = models.CharField(max_length=100)
	date = models.CharField(max_length=15)
	def __str__(self):
		return self.title