from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length= 120) # titles should be this way to limit how much text can go in. Max_length is required
	description = models.TextField(blank= True, null= True) # textfield is fine but What if the user does not want to add a description
	price = models.DecimalField(decimal_places= 2, max_digits= 10000) # could also used float field. View documenation for difference
	summary = models.TextField(blank= True, null= False)
	feature = models.BooleanField(default= False) # can do null= True, default= True

	'''
	def get_absolute_url(self):  # Dynamic linking of Url's
		return f"/products/{self.id}/" 
	'''

	def get_absolute_url(self):  # Url reverse 
		return reverse("products:product", kwargs={"my_id":self.id})

