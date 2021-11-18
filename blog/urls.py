from django.urls import path
from django.urls.resolvers import path
from . import views


URLPattern = [
    path('', views.post_list, name='psot_list'),

]