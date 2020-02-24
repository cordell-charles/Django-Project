from django.contrib import admin
from accounts.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'first_name', 'last_name', 'is_superuser']
	search_fields = ['user__email, user__username']

	def email(self, obj):
		return obj.user.email


admin.site.register(User, UserAdmin)
