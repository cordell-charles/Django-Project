from django.shortcuts import render
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



def article_list_view(request):

	queryset = Article.objects.all() # gives back list of objects
	context = {
		"object_list" : queryset
	}
	return render(request, "articles/article_list.html", context)