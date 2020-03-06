from django.shortcuts import render, redirect, reverse
from django.views.generic import View, ListView, FormView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from .models import BlogUser
from .forms import RegisterForm, LoginForm


class RegisterView(FormView):

	template_name   = 'users/register.html'
	form_class      = RegisterForm

	def form_valid(self, form):
		# SAVE THE USER USING THE FUNCTION THAT YOU CREATED AS STATIC!
		blog_user = BlogUser.create_user(
			first_name=form.cleaned_data.get('first_name'), last_name=form.cleaned_data.get('last_name'),
			email=form.cleaned_data.get('email'), username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'),  
			)
		login(self.request, blog_user.user)
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		for errors in form.errors.items():
			key, msg = errors
			messages.add_message(self.request, messages.ERROR, _(msg[0]))
		return super().form_invalid(form)

	def get_success_url(self):
		return reverse('blog:article-list')


class AccountListView(ListView):
	model = BlogUser
	template_name = 'users/user_list.html'

	def get_queryset(self):
		return BlogUser.objects.all()


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
		blog_user = form.get_user()
		login(self.request, blog_user)
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
