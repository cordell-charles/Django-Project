from django.contrib import admin
from register.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
	list_display = ['user', 'first_name', 'email']
	search_fields = ['user__email, user__username']

	def email(self, obj):
		return obj.user.email


admin.site.register(User, UserAdmin)