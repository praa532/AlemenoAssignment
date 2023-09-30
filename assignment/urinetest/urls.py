from django.contrib import admin
from django.urls import path,include
from urinetest import views

urlpatterns = [
    path("index", views.index, name="Home"),
    path("", views.index, name="Home"),
    path('upload_image/', views.upload_image, name='process_image'),
]