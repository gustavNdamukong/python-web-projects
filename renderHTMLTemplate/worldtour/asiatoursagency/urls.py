from django.urls import path
from .views import index

# import from the current directory
from . import views

# define a list or url patterns
urlpatterns = [
    # path('', views.index),
    path('', index, name="index"),
]