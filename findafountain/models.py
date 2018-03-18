from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify 
from django.utils import timezone

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to='profile_images', blank=True, default='profile_images/default.png')

	def __str__(self):
		return self.user.username

class Fountain(models.Model):
	name = models.CharField(max_length=32, unique=False)
	lat = models.FloatField()
	lng = models.FloatField()
	image = models.ImageField(upload_to='fountain_images', blank=False, default='fountain_images/default2.jpg')
	description = models.CharField(max_length=250, unique=False)
	floor = models.IntegerField(null=False)
	reviews = models.IntegerField(default=0)
	rating = models.IntegerField(default=0)
	numberratings = models.IntegerField(default=0)
	avgrating = models.FloatField(blank=True, null=True, default=0)
	popularity = models.IntegerField(default=0)
	broken = models.BooleanField(default='False')
	building = models.CharField(max_length=32, unique=False, null=True)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.id)
		super(Fountain, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

class Review(models.Model):
	title = models.CharField(max_length=32, unique=False) 
	datetime = models.DateTimeField(("Date"), default=timezone.now)
	text = models.CharField(max_length=250, unique=False) 
	user = models.ForeignKey(UserProfile)
	fountain = models.ForeignKey(Fountain)

	def __str__(self):
		return self.title

class Rating(models.Model): 
	datetime = models.DateTimeField(("Date"), default=timezone.now)
	points = models.IntegerField(default=0, blank=False, null=False)
	user = models.ForeignKey(UserProfile)
	fountain = models.ForeignKey(Fountain, related_name='+')

	def __str__(self):
		return self.fountain.name

# Create your models here.
