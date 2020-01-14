from django import forms
from .models import User
from django.contrib.auth.hashers import check_password
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

	email 			= forms.EmailField(required= True,max_length= 80)
	password 		= forms.CharField(required= True, max_length= 100,  widget=forms.PasswordInput)


	def clean_email(self, email):
		"""
		Validate email against the database
		"""
		try:
			User.objects.get(user__email= email)
		except User.DoesNotExist:
			raise ValueError()
		return

	def clean_password(self, password):
		"""
		To validate you should use the django check_password
		"""
		# user = User.objects.last()
		try:
			check_password(password)
		except:
			raise ValueError()
		return
