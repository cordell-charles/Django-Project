from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import transaction

# Create your models here.
class BlogUser(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_user')

	@property
	def display_name(self):
		return f"{self.user.first_name} {self.user.last_name}"

	def __str__(self):
		return f"{self.user.email}"

	@staticmethod
	def create_user(first_name, last_name, username, email, password):
		try:
			with transaction.atomic():
				user = get_user_model().objects.create(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
				return  BlogUser.objects.create(user=user)
		except Exception as e:
			return e

class profile:
	# id = models.models.ForeignKey("accounts.BlogUser", verbose_name=_("blog profiles"), on_delete=models.CASCADE)
	pass