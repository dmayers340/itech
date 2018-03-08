import django
from django.core.management.base import BaseCommand
from findafountain.models import UserProfile, Fountain

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'our help string comes here'

	def populate(self): 
		fountain1 = Fountain(
			name='Library 4th Floor', 
			lat=55.873248, 
			lng=-4.288996, 
			description='Awkwardly located next to the bathrooms', 
			image='fountain_images/libraryfountain.jpg', 
			floor=4, 
			reviews=0, 
			rating=0, 
			numberratings=0, 
			avgrating=0, 
			popularity=0, 
			broken=False,
			building='Library')
		fountain1.save()

		fountain2 = Fountain(
			name='Boyd Orr 10th Floor', 
			lat=55.873523, 
			lng=-4.292436, 
			description='Drinking water available from sinks in the bathrooms', 
			image='fountain_images/default2.jpg',
			floor=10, 
			reviews=0, 
			rating=0, 
			numberratings=0, 
			avgrating=0, 
			popularity=0, 
			broken=False, 
			building='Boyd Orr Building')
		fountain2.save()

		fountain3 = Fountain(
			name = 'Fraser building',
			lat=55.873197, 
			lng=-4.288235, 
			description='Water fountain like any other. Avoid the queue by getting to it before lunch starts. ', 
			image='fountain_images/default3.png', 
			floor=2, 
			reviews=0, 
			rating=0, 
			numberratings=0, 
			avgrating=0, 
			popularity=0, 
			broken=False, 
			building='Fraser Building')
		fountain3.save()

		fountain4 = Fountain(
			name = 'Wolfson',
			lat=55.873086,
			lng=-4.293131,
			description='The fountain can be found on the ground floor Food outlet. Keep in mind that the place gets manic during lunch', 
			image='fountain_images/default4.png', 
			floor=0, 
			reviews=0, 
			rating=0, 
			numberratings=0, 
			avgrating=0, 
			popularity=0, 
			broken=False, 
			building='Wolfson Medical School Building')
		fountain4.save()

		fountain5 = Fountain(
			name = 'Stupid broken fountain',
			lat=55.873614,
			lng=-4.288864,
			description='This fountain has been broken forever, are they ever going to fix it? Complete shambles!!!!', 
			image='fountain_images/default5.jpeg', 
			floor=3, 
			reviews=0, 
			rating=0, 
			numberratings=0, 
			avgrating=0, 
			popularity=0, 
			broken=True, 
			building='Library')
		fountain5.save()

		fountain6 = Fountain(
			name = 'Hidden basement fountain',
			lat=55.872100,
			lng=-4.291655,
			description='A water basin available next to the bathrooms on the basement level', 
			image='fountain_images/default.png', 
			floor=0, 
			reviews=0, 
			rating=0, 
			numberratings=0, 
			avgrating=0, 
			popularity=0, 
			broken=False, 
			building='Kelvin Building')
		fountain6.save()

		fountain7 = Fountain(
			name = 'Dope fountain',
			lat=55.873716,
			lng=-4.292528,
			description='Next to the vending machines on ground floor', 
			image='fountain_images/default.png', 
			floor=0, 
			reviews=0, 
			rating=0, 
			numberratings=0, 
			avgrating=0, 
			popularity=0, 
			broken=False, 
			building='Boyd Orr Building')
		fountain7.save()

		fountain8 = Fountain(
			name = 'Study fountain',
			lat=55.873397,
			lng=-4.289351,
			description='The water fountain is next to the big windows in the study area', 
			image='fountain_images/default.png', 
			floor=1, 
			reviews=0, 
			rating=0, 
			numberratings=0, 
			avgrating=0, 
			popularity=0, 
			broken=False, 
			building='Library')
		fountain8.save()

	def handle(self, *args, **options):
		self.populate()