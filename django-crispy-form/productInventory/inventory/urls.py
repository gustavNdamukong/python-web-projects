from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('create', views.product_create_view, name="product_create"),
    path('list', views.product_list_view, name="product_list"),

    # how to pass a dynamic URL parameter to a route
        ''' Here is an example of how the id value is passed from a template file 
            as 2nd arg to the 'url' directive, after the target view, which in 
            this case is 'product_update'. 

            <a href="{% url 'product_update' product.product_id %}" 
                class="btn btn-warning btn-lg"
                role="button">
                    Update
            </a> '''
    path('update/<int:product_id>/', views.product_update_view, name="product_update"),
    path('delete/<int:product_id>/', views.product_delete_view, name="product_delete"),
]
        