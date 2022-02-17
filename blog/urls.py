from django.conf import settings
# from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('postComment/', views.postComment, name="postComment"),
    path('<str:slug>/', views.blogPage, name="blogPage"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
