from django.shortcuts import render, redirect
from .form import ContactForm

# Create your views here.
# This form app will contain 3 different HTML pages
'''  
    -A home/landing page where users first visit and click a link to go to form
    -A contact form page where users can fill and submit the form
    -The page where the users are directed to after submitting the form
'''
# This is the home page view function
def home_view(request):
    return render(request, 'form_app/home.html')

# Define the contact_view() function to handle the contact form submission
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
        context = {'form':form}
    return render(request, 'form_app/contact.html', context)


# The contact_success_view function to handle the successful form submission
def contact_success_view(request):
    return render(request, 'form_app/contact_success.html')
    