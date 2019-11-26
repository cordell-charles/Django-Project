from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)

from .models import Article
from .forms import ArticleForm

# Create your views here.

class ArticleDetailView(DetailView):
	template_name = 'articles/article_detail.html'

	def get_object(self):
		id_ = self.kwargs.get("my_id")
		return get_object_or_404(Article, id=id_)



''' Function based detail view
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
'''



def dynamic_lookup_view(request, my_id): # Dynamic Url Routing
	obj = Article.objects.get(id= my_id)
	# obj = get_object_or_404(Product, id= my_id) - Changing the error page layout if object is not found 
	context = {
	"object": obj
	}
	return render(request, "articles/article_detail.html", context)








class ArticleListView(ListView): # Class based list view
	# model = Article
	template_name = 'articles/article_list.html'
	queryset = Article.objects.all()  # blog/<modelname>_list.html


''' Function based list view 

def article_list_view(request):
 
	queryset = Article.objects.all() # gives back list of objects
	context = {
		"object_list" : queryset
	}
	return render(request, "articles/article_list.html", context)
'''







class ArticleCreateView(CreateView): # Class based create view
	# model = Article
	template_name = 'articles/article_create.html'
	form_class = ArticleForm
	queryset = Article.objects.all()

''' # Function based create view
def article_create_view(request):
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
'''



class ArticleEditView(UpdateView): # Class based editing view
	
	template_name = 'articles/article_create.html'
	form_class = ArticleForm

	def get_object(self):
		id_ = self.kwargs.get("my_id")
		return get_object_or_404(Article, id=id_)

	def form_valid(self, form):
		return super().form_valid(form)
















class ArticleDeleteView(DeleteView): # Class based editing view
	
	template_name = 'articles/article_delete.html'
	# form_class = ArticleForm

	def get_object(self):
		id_ = self.kwargs.get("my_id")
		obj = get_object_or_404(Article, id=id_)
		return obj

	def get_success_url(self):
		return reverse('blog:article-list')


'''
 # Function based delete view
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
'''