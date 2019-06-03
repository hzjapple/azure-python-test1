# posts/urls.py
from django.urls import path
from django.conf.urls import url
from posts import views
from .views import HomePageView, CreatePostView # new

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path('home/', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'),  # new
    url(r'^upload/$', views.simple_upload, name='simple_upload'),
]