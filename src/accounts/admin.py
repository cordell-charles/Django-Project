from django.contrib import admin
from accounts.models import BlogUser
# Register your models here.


class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'first_name', 'last_name', 'is_superuser']
	search_fields = ['user__email, user__username']

	def username(self, obj):
		return obj.user.username

	def email(self, obj):
		return obj.user.email

	def first_name(self, obj):
		return obj.user.first_name

	def last_name(self, obj):
		return obj.user.last_name

	def is_superuser(self, obj):
		return obj.user.is_superuser


admin.site.register(BlogUser, UserAdmin)
