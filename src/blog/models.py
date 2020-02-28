from django.db import models
from django.urls import reverse
from accounts.models import BlogUser
from django.utils import timezone

# Create your models here.
class Article(models.Model):
	user		= models.ForeignKey(BlogUser, related_name='articles', on_delete= models.CASCADE)
	title 		= models.CharField(max_length= 120) 
	subtitle 	= models.CharField(max_length= 240)
	date 		= models.DateField(default=timezone.now)
	article 	= models.TextField(blank= False)
	name 		= models.CharField(blank= False, max_length= 80)



	def get_absolute_url(self):  
		return reverse("blog:article-detail", kwargs={"my_id":self.id})


