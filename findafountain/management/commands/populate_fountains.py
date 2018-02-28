import django
from django.core.management.base import BaseCommand
from findafountain.models import UserProfile, Fountain

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'our help string comes here'

	def populate(self): 
		fountain1 = Fountain(
			name='Library 5th Floor', 
			lat=55.873248, 
			lng=-4.288996, 
			description='Awkwardly located next to the bathrooms', 
			image='blank', 
			floor=4, 
			reviews=0, 
			rating=0, 
			numberratings=0, 
			avgrating=0, 
			popularity=0, 
			broken=False)
		fountain1.save()

		fountain2 = Fountain(
			name='Boyd Orr 10th Floor', 
			lat=55.873523, 
			lng=-4.292436, 
			description='Drinking water available from sinks in the bathrooms', 
			image='blank', 
			floor=10, 
			reviews=0, 
			rating=0, 
			numberratings=0, 
			avgrating=0, 
			popularity=0, 
			broken=False)
		fountain2.save()

	def handle(self, *args, **options):
		self.populate()