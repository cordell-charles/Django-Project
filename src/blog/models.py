from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length= 120) 
	subtitle = models.CharField(max_length= 240)
	date = models.DateField(auto_now= True)
	article = models.TextField(blank= False)
	name = models.CharField(blank= False, max_length= 80)


	def get_absolute_url(self):  # Url reverse 
		return reverse("articles:article-detail")
