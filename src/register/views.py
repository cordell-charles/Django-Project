from django.shortcuts import render, redirect
from .models import Users
from .forms import RegisterForm

# Create your views here.
def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid(): 
			form.save()

		return redirect("/home")
	else:
		form = RegisterForm()

	return render(request, "register/register.html", {"form":form})

'''
def product_create_view(request):

	form = ProductForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
		'form' : form
	}
	return render(request, "products/product_create.html", context)
'''



