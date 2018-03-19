from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseNotFound
from django.template import RequestContext
from findafountain.forms import UserForm, UserProfileForm, ReviewForm, RatingForm, FountainForm, BrokenFountainForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse 
from findafountain.models import Fountain
from findafountain.models import Review
from findafountain.models import Rating
from findafountain.models import UserProfile
from django.utils import timezone
from django.contrib import messages


def index(request):
	fountain_list = Fountain.objects.order_by('name').distinct()
	floor_list = Fountain.objects.values('floor').order_by('floor').distinct()
	building_list = Fountain.objects.values('building').order_by('building').distinct()
	reviews = Review.objects.order_by('-datetime')
	ratings = Rating.objects.order_by('-datetime')
	context_dict = {'fountains': fountain_list, 'floors': floor_list, 'reviews': reviews, 'ratings': ratings}
	review_list=list(reviews)
	rating_list=list(ratings)
	recent_activity = sum([review_list, rating_list], [])
	recent_activity.sort(key=lambda item: item.datetime, reverse=True)

	context_dict = {'fountains': fountain_list, 'floors': floor_list, 'buildings': building_list, 'reviews': review_list, 'activity': recent_activity}

	return render(request, 'findafountain/index.html', context_dict)

def get_fountain(request, fountain_id_slug):

	context_dict = {}
	review_form = ReviewForm()
	rating_form = RatingForm()
	brokenfountain_form = BrokenFountainForm()

	if request.method=='POST' and 'reviewform' in request.POST:
		review_form = ReviewForm(request.POST)
		if review_form.is_valid(): 
			review_form = ReviewForm(request.POST)
			review = review_form.save(commit=False)
			review.user = UserProfile.objects.get(user=request.user)
			review.datetime = timezone.now()
			review.fountain = Fountain.objects.get(id=fountain_id_slug)
			review.save() 
			return HttpResponseRedirect(reverse('submitted'))

	if request.method=='POST' and 'ratingform' in request.POST:
		rating_form = RatingForm(request.POST)
		if rating_form.is_valid():
			rating_form = RatingForm(request.POST)
			rating = rating_form.save(commit=False)
			rating.user = UserProfile.objects.get(user=request.user)
			rating.datetime = timezone.now()
			rating.fountain = Fountain.objects.get(id=fountain_id_slug)
			rating.save() 
			return HttpResponseRedirect(reverse('submitted'))

	if request.method == 'POST' and 'broken' in request.POST:
		brokenfountain_form = BrokenFountainForm(request.POST)
		fountain = Fountain.objects.get(id=fountain_id_slug)
		broken = request.POST.get("broken", None) 
		if broken == 'True':
			fountain.broken = True
		elif broken == 'False':
			fountain.broken = False
		fountain.save()
		return HttpResponseRedirect(reverse('submitted'))
					
	try: 
		fountain = Fountain.objects.get(id=fountain_id_slug)
		reviews = Review.objects.filter(fountain=fountain_id_slug).order_by('-datetime')
		ratings = Rating.objects.filter(fountain=fountain_id_slug).order_by('-datetime')

		context_dict['fountain'] = fountain
		context_dict['reviews'] = reviews
		context_dict['ratings'] = ratings
		context_dict['review_form'] = review_form
		context_dict['rating_form'] = rating_form
	except Fountain.DoesNotExist: 
		context_dict['fountain'] = None

	return render(request, 'findafountain/fountain.html', context_dict)

def about(request):
	return render(request, 'findafountain/about.html')

def page_not_found(request):
	return render(request, HttpResponseNotFound, 'findafountain/404.html')

def contact(request):
	return render(request, 'findafountain/contact.html')

def submit(request):
	if request.method =='POST':
		fountain_form = FountainForm(data=request.POST)
		if fountain_form.is_valid():
			fountain = fountain_form.save(commit=False)
			fountain.lat = request.POST.get("latitude", None) 
			fountain.lng = request.POST.get("longitude", None) 
			fountain.save()
			return HttpResponseRedirect(reverse('submitted'))
		else:
			print(fountain_form.errors)
	else:
		fountain_form = FountainForm()

	return render(request, 'findafountain/submit.html', {'fountain_form': fountain_form})	

def submitted(request):
	return render(request, 'findafountain/submitted.html', {})

def register(request):
	registered=False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered = True
			user = user_login(request)
			return HttpResponseRedirect(reverse('index'))
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form=UserProfileForm()

	return render(request,'findafountain/register.html', {'user_form': user_form,
'profile_form': profile_form,
'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Your findafountain account is disabled.")
		else:
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.") 
	else:
		return render(request, 'findafountain/login.html', {})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))


def page_not_found(request):
	data = {}
	return render(request, 'findafountain/404.html', data)

def server_error(request):
	data = {}
	return render(request, 'findafountain/500.html', data)
