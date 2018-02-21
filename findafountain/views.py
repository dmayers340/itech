from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.template import RequestContext
from findafountain.forms import UserForm, UserProfileForm

def index(request):
	return render(request, 'findafountain/index.html')

def about(request):
	return render(request, 'findafountain/about.html')

def page_not_found(request):
	return render(request, HttpResponseNotFound, 'findafountain/404.html')

def contact(request):
	return render(request, 'findafountain/contact.html')

def search(request):
	return render(request, 'findafountain/search.html')

def submit(request):
	return render(request, 'findafountain/submit.html')
	
def login(request):
	return render(request, 'findafountain/login.html')

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