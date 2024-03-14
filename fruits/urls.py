from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('task/', task, name='task'),
    path('sets_of_friuts/', sets_of_fruits, name='sets_of_friuts'),
    path('services/', services, name='services')
]
