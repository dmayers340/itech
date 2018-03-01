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
			rating=12, 
			numberratings=3, 
			avgrating=4, 
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
			name = 'Dining Hall',
			lat=55.873197, 
			lng=-4.288235, 
			description='Water fountain like any other. Avoid the queue by getting to it before the lunch starts. ', 
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
			name = 'Stewart Memorial Fountain',
			lat=55.868075,
			lng=-4.283817,
			description='This is not a drinking fountain, what were you thinking??', 
			image='fountain_images/stewart.jpeg', 
			floor=0, 
			reviews=0, 
			rating=0, 
			numberratings=0, 
			avgrating=0, 
			popularity=0, 
			broken=True, 
			building='')
		fountain4.save()

	def handle(self, *args, **options):
		self.populate()