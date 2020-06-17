from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-page'),
    path('projects/', views.projects, name='projects-page'),
    path('about/', views.about, name='about-page'),
    path('contact/', views.contact, name='contact-page'),
]