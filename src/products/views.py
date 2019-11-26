from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

'''
def product_create_view(request):
	my_form = RawProductForm(request.GET) 
	if request.method == "POST":
		my_form = RawProductForm(request.POST)
		if my_form.is_valid():
			# This is valid data coming in and not disrupted
			print(my_form.cleaned_data)
			Product.objects.create(**my_form.cleaned_data)
		else:
			print(my_form.errors)

	context = {
		"form" : my_form
	}
	return render(request, "products/product_create.html", context)
'''


'''
def product_create_view(request):
	print(request.GET)
	print(request.POST)

	if request.method == "POST":
		my_new_title = request.POST.get('title')
		print(my_new_title)
		# Product.objects.create(title=my_new_title)

	context = {}
	return render(request, "products/product_create.html", context)
'''

def product_list_view(request):
	queryset = Product.objects.all() # gives back list of objects
	context = {
		"object_list" : queryset
	}
	return render(request, "products/product_list.html", context)





def product_delete_view(request, my_id):
	obj = get_object_or_404(Product, id= my_id)
	# POST request
	if request.method == "POST":
		# confirming delete
		obj.delete()
		return redirect('home.html')
	context = {
		"object": obj
	}
	return render(request, "products/product_delete.html", context)




def dynamic_lookup_view(request, my_id): # Dynamic Url Routing
	obj = Product.objects.get(id= my_id)
	# obj = get_object_or_404(Product, id= my_id) - Changing the error page layout if object is not found 
	context = {
	"object": obj
	}
	return render(request, "products/product_detail2.html", context)




def product_create_view(request):

	form = ProductForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
		'form' : form
	}
	return render(request, "products/product_create.html", context)



def product_detail_view(request):

	obj = Product.objects.get(id=1)
	# context = {
		# 'title' : obj.title,
		# 'description' : obj.description
	# }

	context = {
		'object' : obj
	}
	return render(request, "products/product_detail.html", context)
