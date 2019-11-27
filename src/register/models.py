from django.db import models

# Create your models here.

class Users(models.Model):
	first_name 	= models.CharField(blank= False, max_length= 80)
	last_name 	= models.CharField(blank= False, max_length= 80)
	email 		=
	username 	=
	password 	=



# class Article(models.Model):
# 	title = models.CharField(max_length= 120) 
# 	subtitle = models.CharField(max_length= 240)
# 	date = models.DateField(auto_now= True)
# 	article = models.TextField(blank= False)
# 	name = models.CharField(blank= False, max_length= 80)