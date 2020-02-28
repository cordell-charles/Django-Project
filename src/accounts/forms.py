from django import forms
from .models import BlogUser
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _


class RegisterForm(forms.Form):

	first_name 	= forms.CharField(required= True, max_length= 50)
	last_name 	= forms.CharField(required= True, max_length= 50)
	email 		= forms.EmailField(required= True, max_length= 80)
	username 	= forms.CharField(required= True, max_length= 100)
	password 	= forms.CharField(label= 'Password', required= True, max_length= 100, widget= forms.PasswordInput)
	password1	= forms.CharField(label= 'Password Confirmation', required= True, max_length= 100, widget= forms.PasswordInput)

	def clean_password(self):
		password 	= self.cleaned_data["password"].strip()
		if password == None:
			self.add_error('password', _("This field cannot be empty, please enter a password"))
		return password	

	def clean_password_retype(self):
		password1 	= self.cleaned_data["password1"].strip()
		if password1 == None:
			self.add_error('password', _("This field cannot be empty, please enter a password"))
		return password1

	def password_valiadation(self):
		# Validate the two passwords and check to see if they match
		password 	= self.cleaned_data.get("password")
		password1	= self.cleaned_data.get("password1")
		if pasword != password1:
			raise forms.ValidationError("Passwords do not match!")
		return password



class LoginForm(forms.Form):

	email			= forms.EmailField(label=_("email"), required= True, max_length= 80, widget= forms.TextInput(attrs={'placeholder':'email'}))
	password 		= forms.CharField(label=_("password"), required= True, max_length= 100,  widget=forms.PasswordInput(attrs={'placeholder':'password'}))

	def get_user(self):
		return self.auth_user

	def clean(self):
		try:
			email 	 = self.cleaned_data['email'].strip()
			password = self.cleaned_data['password']

			blog_user = BlogUser.objects.get(user__email__iexact=email)

			try:
				self.auth_user = authenticate(username=blog_user.user.username, password=password)
			except ValueError:
				self.auth_user = None
			
			if self.auth_user:
				return self.cleaned_data

		except (BlogUser.DoesNotExist, KeyError):
			raise forms.ValidationError("Your login details were incorrect. Please try again.")

		raise forms.ValidationError("Your login details were incorrect. Please try again.")