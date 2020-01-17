from django import forms
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User



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
		# Check to see if the password entries match
		password 	= self.cleaned_data.get("password")
		password1	= self.cleaned_data.get("password1")
		if password != password1:
			raise forms.ValidationError("Passwords do not match!")
		return password





class LoginForm(forms.Form):

	# email 			= forms.EmailField(required= True,max_length= 80)
	username		= forms.CharField(required= True, max_length= 80)
	password 		= forms.CharField(required= True, max_length= 100,  widget=forms.PasswordInput)


	# def clean_email(email):
	# 	"""
	# 	Validate email against the database
	# 	"""
	# 	try:
	# 		User.objects.get(user__email= email)
	# 	except ObjectDoesNotExist:
	# 		raise forms.ValidationError("User does not exist!")
	# 	return user__email

	# user = authenticate(username=username, password=password)

	def clean_username(self):
		try:
			username= self.cleaned_data['username']
			User.objects.get(username)
			authenticate(user.username)
		except ObjectDoesNotExist:
			raise forms.ValidationError("User does not exist!")
		return username


	def clean_password(self):
		"""
		To validate you should use the django check_password
		"""
		# user = User.objects.last()
		try:
			password= self.cleaned_data['password']
			check_password(password)
			authenticate(user.password)
		except:
			raise forms.ValidationError('Password is incorrect')
		return password

	def get_user(self):
		return self.authed_user