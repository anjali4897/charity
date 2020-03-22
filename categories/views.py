from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
# Create your views here.

def causes(request):
    #filter(cat_id='2')
    queryset= Causes.objects.filter(Q(cat_id='1') | Q(cat_id='2') | Q(cat_id='3'))
    queryset1 = Causes.objects.filter(Q(cat_id='4') | Q(cat_id='5') | Q(cat_id='6'))
    context={"object_list":queryset,"object_list1": queryset1}
    return render(request, 'categories/causes.html',context)

def charity1(request):
    queryset1 = charity_list.objects.filter(Q(causes_id='1'))
    context = {"object_list": queryset1}
    return render(request, 'categories/animal.html',context)

def charity2(request):
    queryset2 = charity_list.objects.filter(Q(causes_id='2'))
    context = {"object_list1": queryset2}
    return render(request, 'categories/environment.html', context)

def charity3(request):
    queryset3 = charity_list.objects.filter(Q(causes_id='3'))
    context = {"object_list2": queryset3}
    return render(request, 'categories/international.html', context)

def charity4(request):
    queryset1 = charity_list.objects.filter(Q(causes_id='4'))
    context = {"object_list": queryset1}
    return render(request, 'categories/health.html', context)

def charity5(request):
    queryset1 = charity_list.objects.filter(Q(causes_id='5'))
    context = {"object_list": queryset1}
    return render(request, 'categories/education.html', context)

def charity6(request):
    queryset1 = charity_list.objects.filter(Q(causes_id='6'))
    context = {"object_list": queryset1}
    return render(request, 'categories/art_culture.html', context)