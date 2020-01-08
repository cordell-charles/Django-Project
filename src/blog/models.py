from django.db import models
from django.urls import reverse
from register.models import User

# Create your models here.
class Article(models.Model):
	# user		= models.ForeignKey(User, on_delete= models.CASCADE)
	title 		= models.CharField(max_length= 120) 
	subtitle 	= models.CharField(max_length= 240)
	date 		= models.DateField(auto_now= True)
	article 	= models.TextField(blank= False)
	name 		= models.CharField(blank= False, max_length= 80)



	def get_absolute_url(self):  
		return reverse("blog:article-detail", kwargs={"my_id":self.id})


