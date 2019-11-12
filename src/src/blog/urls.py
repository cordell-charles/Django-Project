from django.urls import path
from .views import (
    article_detail_view,
    article_list_view,
    article_create_view,
    dynamic_lookup_view,
    )


app_name = 'blog'
urlpatterns = [
    path('<int:my_id>/', dynamic_lookup_view, name= 'article-detail'),
    path('', article_list_view, name= 'article-list'),
    path('create', article_create_view, name= 'article-create')
]





# Product urls examples 

# urlpatterns = [
# 	path('product/', product_detail_view),
#     path('', product_list_view, name= 'product-list' ),
#     path('create/', product_create_view),
#     path('<int:my_id>/', dynamic_lookup_view, name= 'product'),
#     path('<int:my_id>/delete/', product_delete_view, name='product-delete'),
# ]