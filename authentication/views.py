from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from .models import Product

# Create your views here.
@never_cache
@login_required(login_url='login')
def home(request):
  products = Product.objects.all()
  return render(request, 'home.html', {'products': products})

@never_cache
def signin(request):
  if request.user.is_authenticated:
    return redirect('home')
  
  else:
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      
      user = authenticate(username=username, password=password)
      
      if user is not None:
        login(request, user)
        return redirect('home')
        
      else:
        messages.error(request, "Inavlid Username and/or Password")
      
  return render(request, 'login.html')

@never_cache
def signout(request):
  logout(request)
  return redirect('login')
