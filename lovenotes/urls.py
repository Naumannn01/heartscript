from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_note, name='create_note'),
    path('my-notes/', views.my_notes, name='my_notes'),
]
