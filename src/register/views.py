from django.shortcuts import render, redirect, reverse
from django.views.generic import View, ListView, FormView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import RegisterForm, LoginForm

# Create your views here.


def register(request):

	form = RegisterForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			response = redirect("/login")
			return response
	else:
		return render(request,"register/register.html",{"form": form})


class RegisterListView(ListView):
	model = User
	template_name = 'register/user_list.html'
	queryset = User.objects.all()




class LoginView(FormView):
	'''
	Signing in existing users while also checking if they already have a session open
	'''
	template_name = 'register/login.html'
	form_class = LoginForm
	# import ipdb;ipdb.set_trace()

	def get(self, request):
		if request.user.is_authenticated:
			return HttpResponseRedirect(self.get_success_url())
		print('made the request')
		return render(request, 'register/login.html', {"form": self.form_class})


	def form_valid(self, form):
		# import ipdb;ipdb.set_trace()
		print('made it here')
		# user = authenticate(username, password)
		user = get_user()
		login(request, user)
		return HttpResponseRedirect(self.get_success_url())


	def form_invalid(self, form):
		"""
		If form is not valid, then this function is ran
		"""
		# import ipdb; ipdb.sset_trace()
		messages.add_message(self.request, messages.ERROR, ("Username or password is invalid!"))
		return render(self.request, 'register/login.html', {"form": self.form_class})


	def get_success_url(self):
		return reverse('blog:article-list')



class LogoutView(View):

	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse('login'))

	def logout(self, request):
		logout(request)
		return HttpResponseRedirect('You have been successfully logged out!')

