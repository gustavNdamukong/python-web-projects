# Let's start by creating a form to add a product record 
# in your Product table as specified in the models.py file
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    # this Meta class is used to spec all the attributes our data
    # to help Django forms assoc the right DB table fields with the 
    # right model. As you would imagine, it needs to know the name 
    # of you model, and all its corresponsing table's fields
    class Meta:
        model = Product
        # the __all__ means all the DB table's fields
        fields = '__all__'

        # the labels is a dictionary to spec how you wish for the data 
        # to be represented when fetched & displayed. The keys must match the 
        # exact names you gave your table fields in models.py  
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }

        # Used to spec the widget to be used to render the form fields 
        # Each field in the form will be assoc with a spec input widget
        # eg a number widget for fields that need numbers eg SKU, price 
        # & qty, and a text widget for name & supplier fields etc
        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder':'e.g. 1', 'class':'form-control'}),
            'name': forms.TextInput(attrs={'placeholder':'e.g. shirt', 'class':'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder':'e.g. S12345', 'class':'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder':'e.g. 19.99', 'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder':'e.g. 10', 'class':'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder':'e.g. ABC Corp', 'class':'form-control'}),
        }