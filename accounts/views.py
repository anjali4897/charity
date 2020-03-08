from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import CreateUserForm


def signup_info(request):
    form = CreateUserForm()


    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CreateUserForm()
    context = {'form': form}
    return render(request, 'accounts1/signup.html',context)


def login_info(request):


    '''if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('accounts:signup')
    else:
        form = AuthenticationForm()    {'form':form}'''
    return render(request, 'accounts1/login.html')