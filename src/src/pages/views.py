from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	# return HttpResponse("<h1> Hello World </h1>") string of html
	return render(request, "home.html", {}) # context dictionary


def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
	my_context = {
		"Title": "This is about us", #Use of django documentation template tags and filters
		"my_number": 123,
		"my_list" : [123, 432, 54353, 43254543, 12, 47639],
		"my_html" : "<h1> Html text </h1>" # will pass html tags into site naturally but 'safe' template tag can prevent this 
	}
	return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
	return HttpResponse("<h1> social page </h1>")