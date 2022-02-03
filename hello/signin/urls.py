from django.urls import path
from signin import views

urlpatterns = [
    path("", views.loginUser, name = 'login'),
]