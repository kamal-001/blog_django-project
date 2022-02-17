from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handeLogin, name="handleLogin"),
    path('logout/', views.handelLogout, name="handleLogout"),
    # path('<str:slug>/', include('blog.urls')),
    # path('<str:slug>/', views.blogPage, name="blogPage"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)