from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction

# Create your models here.

class User(models.Model):
	''' User model '''
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null= True, blank= False, on_delete= models.CASCADE)
	first_name = models.CharField(max_length= 50, blank= True, null= True)
	last_name 	= models.CharField(max_length= 50, blank= True, null= True)
	email 		= models.EmailField(max_length= 80, blank= False, null= True)
	username 	= models.CharField(max_length= 100, blank= False, null= True)
	password 	= models.CharField(max_length= 100, blank= False, null= True)

	def __repr__(self):
		return f"(self.user.email)"

	@staticmethod
	def create_user(first_name, last_name, username, email, password):
		with transaction.atomic():
			try:
				user = get_user_model().objects.create(username= username, email= email, password= password)
				User.objects.create(user= user, first_name= first_name, last_name= last_name, email= email,username= username, password= password)
			except Exception as e:
				return e