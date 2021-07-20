from django.urls import path

from . import views

urlpatterns = [
    path('tourist', views.index, name='index'),
    path('',views.button, name='button'),
]