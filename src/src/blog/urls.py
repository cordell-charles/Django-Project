from django.urls import path
from .views import (
    article_detail_view,
    ArticleList,
    article_create_view,
    article_delete_view,
    dynamic_lookup_view,
    )


app_name = 'blog'
urlpatterns = [
    path('<int:my_id>/', dynamic_lookup_view, name= 'article-detail'),
    path('', ArticleList.as_view(), name= 'article-list'),
    path('create', article_create_view, name= 'article-create'),
    path('delete/<int:my_id>/', article_delete_view, name= 'article-delete')
]

