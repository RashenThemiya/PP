from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('posts/', views.posts, name='posts'),
    path('contact/', views.contact, name='contact'),
]
