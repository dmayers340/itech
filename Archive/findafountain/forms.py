#Forms isn't needed but helps with tidyness, could otherwise put in models.py
#1.) Create a model form class for each model to be rep as form
#2.) Customize forms
#3.) Create/update view to handle form
	#need to display form
	#need to save form data
	#need to flag errors if user input wrong info
#4.) Create/update template to display form
#5.) Add urlpatter to map to new view

#1.) ModelForm-helper class to create form from pre-existing model
from django import forms
from django.contrib.auth.models import User
from findafountain.models import UserProfile


class UserForm(forms.ModelForm):
	password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'size':40, 'placeholder':'Password'}))
	username = forms.CharField(label='', widget=forms.TextInput(attrs={'help_text':None,'size':40, 'placeholder':'Username'}))
	class Meta:
		model = User
		fields =('username', 'email',)
		labels={'email':'',}
		widgets ={
			#'username': forms.TextInput(attrs={'help_text':None, 'size':40, 'placeholder':'Username'}),
			'email': forms.TextInput(attrs={'size':40,'placeholder':'Email'}),
		}

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		#fields = ('website', 'picture')
		fields = ('picture',)
