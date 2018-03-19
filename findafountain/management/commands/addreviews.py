import django
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from findafountain.models import UserProfile, Fountain, Review, Rating

class Command(BaseCommand):
	args = '<foo bar ...>'
	help = 'our help string comes here'

	def populate(self): 

		rating5 = Rating(
			points = 3,
			user = UserProfile.objects.get(user=User.objects.get(id=5)), 
			fountain = Fountain.objects.get(id=8), 
			)
		rating5.save()

		rating6 = Rating(
			points = 1,
			user = UserProfile.objects.get(user=User.objects.get(id=5)), 
			fountain = Fountain.objects.get(id=2), 
			)
		rating6.save()

		rating8 = Rating(
			points = 4,
			user = UserProfile.objects.get(user=User.objects.get(id=2)), 
			fountain = Fountain.objects.get(id=3), 
			)
		rating8.save()

		rating9 = Rating(
			points = 1,
			user = UserProfile.objects.get(user=User.objects.get(id=3)), 
			fountain = Fountain.objects.get(id=2), 
			)
		rating9.save()

		rating10 = Rating(
			points = 4,
			user = UserProfile.objects.get(user=User.objects.get(id=5)), 
			fountain = Fountain.objects.get(id=3), 
			)
		rating10.save()

		review1 = Review(
			title = 'Disgusting',
			text = 'Made my stomach upset. Never drinking from these again.',
			fountain = Fountain.objects.get(id=2), 
			user = UserProfile.objects.get(user=User.objects.get(id=1)),
			)
		review1.save()

		rating1 = Rating(
			points = 3,
			user = UserProfile.objects.get(user=User.objects.get(id=1)), 
			fountain = Fountain.objects.get(id=4), 
			)
		rating1.save()

		rating2 = Rating(
			points = 1,
			user = UserProfile.objects.get(user=User.objects.get(id=2)), 
			fountain = Fountain.objects.get(id=5), 
			)
		rating2.save()

		review2 = Review(
			title = 'Fresh cold drinking water',
			text = 'Spent an hour queuing with 1st year undergrad students but totally worth the wait. Super easy to find.',
			fountain = Fountain.objects.get(id=3), 
			user = UserProfile.objects.get(user=User.objects.get(id=2)), 
			)
		review2.save()

		review3 = Review(
			title = 'OK',
			text = 'OK water fountain, like all the others at the library. Water was cold.',
			fountain = Fountain.objects.get(id=1), 
			user = UserProfile.objects.get(user=User.objects.get(id=3)), 
			)
		review3.save()


		rating7 = Rating(
			points = 1,
			user = UserProfile.objects.get(user=User.objects.get(id=4)), 
			fountain = Fountain.objects.get(id=2), 
			)
		rating7.save()

		review4 = Review(
			title = 'Not good',
			text = "Smells like dishwater!! I'd rather climb down the stairs to the ground floor fountain",
			fountain = Fountain.objects.get(id=2), 
			user = UserProfile.objects.get(user=User.objects.get(id=4)), 
			)
		review4.save()

		rating3 = Rating(
			points = 5,
			user = UserProfile.objects.get(user=User.objects.get(id=3)), 
			fountain = Fountain.objects.get(id=6), 
			)
		rating3.save()

		review5 = Review(
			title = 'Hidden gem',
			text = 'Woah! Never knew there was one in the basement until I started using Find a Fountain',
			fountain = Fountain.objects.get(id=6), 
			user = UserProfile.objects.get(user=User.objects.get(id=5)), 
			)
		review5.save()

		review6 = Review(
			title = 'Impossible to find',
			text = 'What the what. Spent hours going in circles because this was behind a bookcase',
			fountain = Fountain.objects.get(id=8), 
			user = UserProfile.objects.get(user=User.objects.get(id=1)), 
			)
		review6.save()

		rating4 = Rating(
			points = 5,
			user = UserProfile.objects.get(user=User.objects.get(id=4)), 
			fountain = Fountain.objects.get(id=7), 
			)
		rating4.save()

		review7 = Review(
			title = "I think I'm dying",
			text = 'Oh my god. What was in that water?',
			fountain = Fountain.objects.get(id=4), 
			user = UserProfile.objects.get(user=User.objects.get(id=2)), 
			)
		review7.save()


		rating11 = Rating(
			points = 3,
			user = UserProfile.objects.get(user=User.objects.get(id=3)), 
			fountain = Fountain.objects.get(id=1), 
			)
		rating11.save()

		review8 = Review(
			title = "Just drinkable",
			text = 'Meh. Not much to say.',
			fountain = Fountain.objects.get(id=2), 
			user = UserProfile.objects.get(user=User.objects.get(id=2)), 
			)
		review8.save()

	def handle(self, *args, **options):
		self.populate()