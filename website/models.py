from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=255)
	content = models.CharField(max_length=255)
	
	def _unicode_(self):
		return self.title

class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	
	def _unicode_(self):
		return self.title
	
class ImageStore(models.Model):
	
	name = models.CharField(max_length=150, null=True)
	
	img = models.ImageField(upload_to='img')


class Meta:
	db_table = 'ImageStore'

# Create your models here.
