from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __str__(self):
		return self.user.username

class Fountain(models.Model):
	name = models.CharField(max_length=32, unique=False)
	lat = models.FloatField()
	lng = models.FloatField()
	image = models.ImageField(upload_to='fountain_images', blank=True)
	description = models.CharField(max_length=250, unique=False)
	floor = models.IntegerField(default=0)
	reviews = models.IntegerField(default=0)
	rating = models.IntegerField(default=0)
	numberratings = models.IntegerField(default=0)
	avgrating = models.FloatField(default=0)
	popularity = models.IntegerField(default=0)
	broken = models.BooleanField(default='false')

	def __str__(self):
		return self.name

# Create your models here.
