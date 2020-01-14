from django.shortcuts import render, redirect
from django.views.generic import View, ListView, FormView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
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
	form_class = LoginForm

	def get(self, request):
		return render(request, 'register/login.html', {"form": self.form_class})


	def form_valid(self, form):
		import ipdb; ipdb.sset_trace()
		email = form.data['email']
		password = form.data['password']


		# user = authenticate(email= email, password= password)
		# if user is not None:
		# 	if user.is_active:
		# 		login(request, user)
		# 		return HttpResponseRedirect('blog/')
		# 	else:
		# 		# Prompt to say account is not active
		# 		return HttpResponse("This account is not active!")
		# else:
		# 	# Returning an incorrect credential error
		# 	print(" Invalid email or password, please try again ")
		# 	return render(request, 'register/login.html')  #, {"form":form})

	def form_invalid(self):
		"""
		If form is not valid, then this function is ran
		"""
		pass


class LogoutView(View):

	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse('login'))

	def logout(self, request):
		logout(request)
		return HttpResponseRedirect('You have been successfully logged out!')

