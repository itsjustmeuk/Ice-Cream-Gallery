from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("about/", views.about, name = 'about'),
    path("services/", views.services, name = 'services'),
    path("error/", views.error, name = 'error'),
]