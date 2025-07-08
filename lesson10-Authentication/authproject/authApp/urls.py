
from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home_view, name='home'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register_view, name='register'), 
    path('protected/', views.ProtectedView.as_view(), name='protected'), 
]