from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Article
from .forms import ArticleForm

# Create your views here.

def article_detail_view(request):

	obj = Article.objects.get()
	# context = {
		# 'title' : obj.title,
		# 'description' : obj.description
	# }

	context = {
		'object' : obj
	}
	return render(request, "articles/article_detail.html", context)



def dynamic_lookup_view(request, my_id): # Dynamic Url Routing
	obj = Article.objects.get(id= my_id)
	# obj = get_object_or_404(Product, id= my_id) - Changing the error page layout if object is not found 
	context = {
	"object": obj
	}
	return render(request, "articles/article_detail.html", context)



'''
def article_list_view(request):
 
	queryset = Article.objects.all() # gives back list of objects
	context = {
		"object_list" : queryset
	}
	return render(request, "articles/article_list.html", context)
'''

class ArticleList(ListView):
	model = Article



def article_create_view(request): # Function based views

	form = ArticleForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = ArticleForm()
		response = redirect('http://127.0.0.1:8000/blog/')

		return response

	context = {
		'form' : form
	}
	return render(request, "articles/article_create.html", context)



def article_delete_view(request, my_id):
	obj = get_object_or_404(Article, id= my_id)
	# POST request
	if request.method == "POST":
		# confirming delete
		obj.delete()
		response = redirect('http://127.0.0.1:8000/blog/')
		return response

	context = {
		"object": obj
	}
	return render(request, "articles/article_delete.html", context)

