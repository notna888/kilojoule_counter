from django.urls import path

from . import views

urlpatterns = [
    path('all', views.all_ingredients, name='all_ingredients'),
    path('load', views.load_ingredients, name='load_ingredients'),
]
