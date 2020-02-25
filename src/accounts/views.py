from django.shortcuts import render, redirect, reverse
from django.views.generic import View, ListView, FormView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from .models import User
from .forms import RegisterForm, LoginForm

# Create your views here.


def login_and_handle_data_stored_in_session(user, request):
	session_key = request.session.session_key
	login(request, user)



class RegisterView(FormView):

	template_name   = 'users/register.html'
	form_class      = RegisterForm

	
	def form_valid(self, form):
		form = RegisterForm(self.request.POST or None)
		if self.request.method == "POST":
			if form.is_valid():
				form.save()
				return HttpResponseRedirect(self.get_success_url())
			else:
				raise forms.ValidationError("Account could not be created, Please try again")
		else:
			return render(request,"users/register.html",{"form": form})


	def form_invalid(self, form):
		for errors in form.errors.items():
			key, msg = errors
			messages.add_message(self.request, messages.ERROR, _(msg[0]))
			return super().form_invalid(form)


	def get_success_url(self):
		return reverse('login')





class AccountListView(ListView):
	model = User
	template_name = 'users/user_list.html'
	queryset = User.objects.all()





class LoginView(FormView):
	'''
	Signing in existing users while also checking if they already have a session open
	'''
	template_name = 'users/login.html'
	form_class = LoginForm

	def get(self, request):
		if request.user.is_authenticated:
			return HttpResponseRedirect(self.get_success_url())
		return render(request, 'users/login.html', {"form": self.form_class})


	def form_valid(self, form):
		print('here')
		import ipdb;ipdb.set_trace()
		user = form.get_user()
		login_and_handle_data_stored_in_session(user, self.request)
		return HttpResponseRedirect(self.get_success_url())


	def form_invalid(self, form):
		"""
		If form is not valid, then this function is ran
		"""
		messages.add_message(self.request, messages.ERROR, ("Email or password is invalid!"))
		return render(self.request, 'users/login.html', {"form": self.form_class})


	def get_success_url(self):
		return reverse('blog:article-list')



class LogoutView(View):

	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse('login'))
