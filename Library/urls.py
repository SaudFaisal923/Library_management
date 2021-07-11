"""BookStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from Book_store import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.register,name='register'),
    path('login/',views.Login,name='login'),
    path('login/books/',views.BookView,name='bookview'),
    path('issuebook/<int:id>/',views.Issue_Book_to_user,name='issuebook'),
    path('mybooks/',views.MyBooks,name='mybooks'),
]
