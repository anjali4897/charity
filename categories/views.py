from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def causes(request):
    queryset= Causes.objects.all()
    context={"object_list":queryset}
    return render(request, 'categories/causes.html',context)