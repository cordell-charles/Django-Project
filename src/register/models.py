from django.db import models

# Create your models here.

class Users(models.Model):
	first_name 	= models.CharField(blank= False, max_length= 50)
	last_name 	= models.CharField(blank= False, max_length= 50)
	email 		= models.EmailField(blank= False, max_length= 80)
	username 	= models.CharField(blank= False, max_length= 100)
	password 	= models.CharField(blank= False, max_length= 100)

