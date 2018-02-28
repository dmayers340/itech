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
			image=null, 
			floor=4, 
			reviews=0, 
			rating=0, 
			numberratings=0, 
			avgrating=0, 
			popularity=0, 
			broken='false')
		fountain1.save() 

	def handle(self:
		self._populate()