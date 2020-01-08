from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    ArticleDetailView,
    ArticleListView,
    ArticleCreateView,
    ArticleEditView,
    ArticleDeleteView,
    dynamic_lookup_view,
    )


app_name = 'blog'
urlpatterns = [
    path('<int:my_id>/', ArticleDetailView.as_view(), name= 'article-detail'),
    path('', ArticleListView.as_view(), name= 'article-list'),
    path('create', ArticleCreateView.as_view(), name= 'article-create'),
    path('edit/<int:my_id>/', ArticleEditView.as_view(), name= 'article-edit'),
    path('delete/<int:my_id>/', ArticleDeleteView.as_view(), name= 'article-delete')
]

