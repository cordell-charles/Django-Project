"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from accounts.views import (RegisterView,
                            AccountListView,
                            LoginView,
                            LogoutView,
    )

from pages.views import (home_view,
    contact_view,
    about_view
    )

urlpatterns = [

    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('products/', include('products.urls')), 
    path('', home_view, name='home'),
    path('about/',about_view),
    path('contact/', contact_view),
    path('register/', RegisterView.as_view(), name='register'),
    path('account-list', AccountListView.as_view(), name= 'account-list'),
    path('login/', LoginView.as_view(), name= 'login'),
    path('logout/', LogoutView.as_view(), name= 'logout')
]
