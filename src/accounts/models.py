from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import transaction

# Create your models here.


class User(AbstractUser):
	''' User model '''
	user 		= models.OneToOneField(settings.AUTH_USER_MODEL, null= True, blank= True, on_delete= models.CASCADE, related_name= 'users')
	first_name 	= models.CharField(max_length= 50, blank= False, null= True)
	last_name 	= models.CharField(max_length= 50, blank= False, null= True)
	email 		= models.EmailField(max_length= 80, blank= False, null= True, unique= True)
	username 	= models.CharField(max_length= 100, blank= False, null= True)
	password 	= models.CharField(max_length= 100, blank= False, null= True)

	class Meta:
		verbose_name_plural = "Blog Users"

	def __repr__(self):
		return f"(self.user.email)"

	USERNAME_FIELD 		= 'email'

	REQUIRED_FIELDS 	= ['first_name', 'last_name', 'username']


	@staticmethod
	def create_user(first_name, last_name, username, email, password= None):
		with transaction.atomic():
			try:
				user = get_user_model().objects.create(username= username, email= email, password= password)
				User.objects.create(user= user, first_name= first_name, last_name= last_name, email= email,username= username, password= password)
			except Exception as e:
				return e


