from django.shortcuts import render, redirect

# Create your views here.
from .forms import ProductForm
from .models import Product

# CRUD views we need
# --------
# Create, 
# Read, 
# Update, 
# Delete

# Home View
def home_view(request):
    return render(request, 'inventory/home.html')


# Create View
def product_create_view(request):
    form = ProductForm()
    # check if new product form is submitted
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # save to the DB
            form.save()
            # show all products after adding new product. 
            return redirect('product_list')
    # if form is not submitted, show user form page to create new product
    return render(request, 'inventory/product_form.html', {'form':form})


# Read View (grab & display all products from DB)
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products':products})


# Update View (grab a product by its id from DB & update)
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)

    # how we populate form with model (DB) data 
    form = ProductForm(instance=product)

    if request.method == "POST":
        # bind product data from the request to the existing product instance
        # how we couple data via an update form with model (DB) 
            # data for DB update. 
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            # save updated form data to DB
            form.save() 
            return redirect('product_list')
    return render(request, 'inventory/product_form.html', {'form':form})


# Delete View (grab a product by its id from DB to delete)
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id=product_id)

    if request.method == "POST":
        product.delete() 
        return redirect('product_list')
    # Let user confirm the delete action before we proceed
    return render(request, 'inventory/product_confirm_delete.html', {'product':product})

