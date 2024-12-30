from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_resume, name='create_resume'),
    path('list/', views.resume_list, name='resume_list'),
]
