from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, NewPassword, NewNote

import string
import random

class vault_users(UserCreationForm):
	# emriLenda = forms.CharField()
	email = forms.EmailField()
	class Meta:
		model = User
		labels = {
			"username": "Username",
			"email": "Email",
			"first_name":"First Name",
			"last_name":"Last Name",
			"password1":"Password",
			"password2":"Confirm Password",
        }
		fields = ['username','email','first_name','last_name','password1','password2']


class newNoteForm(forms.ModelForm):

	class Meta:
		model = NewNote
		labels = {
			"titulli": "Title/Subject",
			"pershkrimi": "Body",
			"files":"Upload Files",
        }
		fields = ["titulli","pershkrimi","files"]



class UserUpdate(forms.ModelForm):

	email = forms.EmailField()
	class Meta:
		model = User
		labels = {
			"username": "Username",
			"email": "Email",
        }
		fields = ['username','email']

class ProfileUpdate(forms.ModelForm):

	class Meta:
		model = Profile		
		fields = ['image']


