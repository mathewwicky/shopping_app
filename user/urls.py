from django.contrib import admin
from django.urls import path
from .import views
from django.contrib.auth import views as authentication_views

app_name = 'user'
urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/',views.profile,name='profile'),
   ]