from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import View
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
    )
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from orders.models import Order, OrderItem

def UserLogin (request):
    print(request.user.is_authenticated())
    title = 'Login'
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        print(request.user.is_authenticated())
        return redirect('/')
    return render(request, 'staff/login_form.html', {'form':form, 'title':title})

def UserLogout (request):
    logout(request)
    return redirect('/')

@login_required(login_url='/account/login/')
def ListOrders (request):
    orders = Order.objects.all()
    orderItem = OrderItem.objects.all()
    return render(request, 'staff/staff_panel.html', {'orders':orders,
                                                      'orderItem':orderItem,
                                                      })
