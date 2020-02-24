from django import forms
from .models import User
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _




class RegisterForm(forms.ModelForm):

	first_name 	= forms.CharField(required= True, max_length= 50)
	last_name 	= forms.CharField(required= True, max_length= 50)
	email 		= forms.EmailField(required= True, max_length= 80)
	username 	= forms.CharField(required= True, max_length= 100)
	password 	= forms.CharField(label= 'Password', required= True, max_length= 100, widget= forms.PasswordInput)
	password1	= forms.CharField(label= 'Password Confirmation', required= True, max_length= 100, widget= forms.PasswordInput)


	class Meta:
		model 	= User
		fields 	= {
			"first_name",
			"last_name",
			"username",
			"email",
			"password"
		}

	def clean_password(self):
		password 	= self.cleaned_data['password'].strip()
		if password == None:
				self.add_error('password', _("This field cannot be empty, please enter a password"))
		print(password)
		return password

	def clean_password_retype(self):
		password1 	= self.cleaned_data['password1'].strip()
		if password1 == None:
			self.add_error('password', _("This field cannot be empty, please enter a password"))
		print(password1)
		return password1


	def password_validation(self):
		# Validate the two passwords and check to see if they match
		password 	= self.cleaned_data.get("password")
		password1	= self.cleaned_data.get("password1")

		if password != password1:
			raise forms.ValidationError("Passwords do not match!")
		return password




class LoginForm(forms.Form):

	email			= forms.EmailField(label=_("email"), required= True, max_length= 80, widget= forms.TextInput(attrs={'placeholder':'email'}))
	password 		= forms.CharField(label=_("password"), required= True, max_length= 100,  widget=forms.PasswordInput(attrs={'placeholder':'password'}))

	class Meta:
		model = User


	def clean(self):
		try:
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			print(email)
			print(password)
			user = get_user_model().objects.get(email= email)
			try:
				self.authed_user = authenticate(email= user.email, password= password)
			except ValueError:
				self.authed_user = None
			if self.authed_user:
				return self.cleaned_data

		except (get_user_model().DoesNotExist, KeyError):
			pass

		raise forms.ValidationError("Your login details were incorrect. Please try again.")



	def get_user(self):
		print('user')
		return self.authed_user
