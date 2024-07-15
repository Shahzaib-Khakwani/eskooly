# myapp/views.py
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView 
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect



def index(request):
    return render(request, 'index.html')

def pages_profile_settings(request):
    return render(request, 'pages-profile-settings.html')

def app_chat(request):
    return render(request, 'apps-chat.html') 

def apps_tasks_kanban(request):
    return render(request, 'apps-tasks-kanban.html') 

def pages_faqs(request):
    return render(request, 'pages-faqs.html') 

def profile_page(request):
    return render(request, 'pages-profile.html') 

def auth_lockscreen_basic(request):
    return render(request, 'auth-lockscreen-basic.html')

def auth_logout_basic(request):
    return render(request, 'auth-logout-basic.html')

def pages_search_results(request):
    return render(request, 'pages-search-results.html')

def ecommerce_products(request):
    return render(request, 'apps-ecommerce-products.html')

def ecommerce_product_details(request):
    return render(request, 'apps-ecommerce-product-details.html')

def ecommerce_checkout(request):
    return render(request, 'apps-ecommerce-checkout.html')

def institute_profiles(request):
    return render(request, 'institute-profiles.html')

# ++++++++++++++++++++++++++++++++


