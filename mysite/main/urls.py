# define paths to different web pages
from django.urls import path

from . import views

# if in the home directory of the site, display the view.index page
app_name = 'mysite'

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("products/", views.products, name="products"),
    path("register/", views.register, name="register"),
    path('testlang', views.testlang, name='testlang'),
]

