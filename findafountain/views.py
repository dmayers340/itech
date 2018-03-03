from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseNotFound
from django.template import RequestContext
from findafountain.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse 
from findafountain.models import Fountain

def index(request):
	fountain_list = Fountain.objects.order_by('name').distinct()
	floor_list = Fountain.objects.order_by('floor').distinct()
	context_dict = {'fountains': fountain_list, 'floors': floor_list}
	return render(request, 'findafountain/index.html', context_dict)

def get_fountain(request, fountain_id_slug):
	context_dict = {}
	try: 
		fountain = Fountain.objects.get(id=fountain_id_slug)
		context_dict['fountain'] = fountain
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
	return render(request, 'findafountain/submit.html')
	

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

