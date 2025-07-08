from django.urls import path

# import from the current directory
from . import views

# define a list or url patterns
urlpatterns = [
    path('', views.index)
]