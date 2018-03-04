import django
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from findafountain.models import UserProfile, Fountain, Review 

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'our help string comes here'

	def populate(self): 
		review1 = Review(
			title = 'Lorem ipsum',
			text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ',
			fountain = Fountain.objects.get(id=1), 
			user = UserProfile.objects.get(user=User.objects.get(id=3)))
		review1.save()

	def handle(self, *args, **options):
		self.populate()