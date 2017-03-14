from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Publication(models.Model):
	pub = models.CharField(max_length=100)
		
	def __unicode__(self):
		return self.pub


class Book(models.Model):
	book = models.CharField(max_length=100)
	pub_id = models.OneToOneField(Publication)
	
	def __unicode__(self):
		return self.book


class Publication_MM(models.Model):
	pub = models.CharField(max_length=100)

	def __unicode__(self):
		return self.pub

class Book_MM(models.Model):
	book = models.CharField(max_length=100)
	pub_id = models.ManyToManyField(Publication_MM)
	
	def __unicode__(self):
		return self.book

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='user_profile')
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	age = models.IntegerField()
	address = models.CharField(max_length=100)
	
