from django.db import models
from django import forms

# Create your models here.
class Note(models.Model):
	title = models.CharField(max_length = 200)
	complete = models.BooleanField(default = False)
	created = models.DateTimeField(auto_now_add=True)
	

	def __str__(self):
		return self.title

class Weather(models.Model):
	city = models.CharField(max_length = 200)
	def __str__(self):
		return self.city

class SecureData(models.Model):
	service = models.CharField(max_length=50)
	api_key = models.CharField(max_length = 200)

	def __str__(self):
		return self.service
		
