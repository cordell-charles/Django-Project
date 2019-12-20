from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import User
from .forms import RegisterForm

# Create your views here.


def register(request):

	form = RegisterForm(request.POST)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			response = redirect("/blog")
			return response
	else:
		return render(request,"register/register.html",{"form": form})


class RegisterListView(ListView):
	model = User
	template_name = 'register/user_list.html'
	queryset = User.objects.all()

