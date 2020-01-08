from django.shortcuts import render, redirect
from django.views.generic import View, ListView, FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import RegisterForm

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


'''
class LoginView(FormView):
	
	Signing in existing users while also checking if they already have a session open
	

	def user_login(self, request):
		form = LoginForm(request.POST or None)
		if request.method == 'POST':
			email = request.POST['email']
			password = request.POST['password']
			sign_in = authenticate(email= email, password= password)
			if sign_in is not None:
				if sign_in.is_active:
					login(request, sign_in)
					return redirect('blog/')
				else:
					# Prompt to say account is not active
					return "This account is not active!"
			else:
				# Returning an incorrect credential error
				print(" Invalid email or password, please try again ")
				return render(request, 'login.html', {"form":form})


	def authenticated(self):
		
		Checks if user is already authenticated
		
'''
'''
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(self.request)
        return HttpResponseRedirect(reverse('login'))
'''