# To handle views and redirects
from django.shortcuts import render, redirect

# To import auth functions from Django
from django.contrib.auth import authenticate, login, logout

# The login_required decorator to protect views
# decorators in python are special funcs that modify the behaviours of other 
# methods/funcs. They're typically used to add additional functionality eg as in this 
# eg login, logout etc without changing the function's code
from django.contrib.auth.decorators import login_required 

# mixins are re-usable classes that can add specific functionality to class-based 
# views (CBV) without being the primary parent class (similar to traits in PHP)
# Class-based views & Function views do same thing-one used classes, the other uses funcs.
# LoginRequiredMixin is used to verify if the current user is authenticated 
from django.contrib.auth.mixins import LoginRequiredMixin

# For class-based views (CBV)
from django.views import View 

# Import the User model (we'll use it to store/persist the data of an authenticated user)
from django.contrib.auth.models import User

# import the RegisterForm form (the one we just created) from forms.py
from .forms import RegisterForm



# Create your views here.
def register_view(request):
    # check if the request method is POST or not (we expect post)
    if request.method == 'POST':
        # this is how you retrieve data submitted via post in a specific form
        form = RegisterForm(request.POST)
        if form.is_valid():
            # success: create user, log in, redirect
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request, user)

            # Here's how to redirect the user to a diff view (here after logging them in)
            return redirect('home')

        # if form is not valid, show the form again with errors
        return render(request, 'accounts/register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    error_message = ""
    if request.method == 'POST':
        # How you retrieve data submitted via post, but not to a specific form
        username = request.POST.get("username")
        password = request.POST.get("password")

        # How to authenticate an existing user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid Credentials!"
    return render(request, 'accounts/login.html', {'error':error_message})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        return redirect('home')
    

    

# The decorator here will only allow access to logged in users 
@login_required
def home_view(request):
    return render(request, 'auth1_app/home.html')


# Protected view
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login'

    # 'next' - to redirect URL
    redirect_field_name = 'redirect_to'

    def get(self, request):
        return render(request, 'registration/protected.html')