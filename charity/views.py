
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def homepage(request):
    return render(request, 'charity_home.html')

def about(request):
    return render(request, 'about.html')

def base(request):
    return render(request, 'base_layout.html')

def causes(request):
    return render(request, 'causes.html')