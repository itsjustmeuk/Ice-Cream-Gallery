from django.urls import path
from signup import views

urlpatterns = [
    path("", views.register, name = 'register'),
]