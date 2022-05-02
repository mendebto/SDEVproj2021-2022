# define paths to different web pages
from django.urls import path

from . import views
# from mysite.views import *

# if in the home directory of the site, display the view.index page
app_name = 'mysite'
urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path('testlang', views.testlang, name='testlang'),
    # path("v1/", views.v1, name="view 1"),
]
