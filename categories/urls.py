from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views


app_name='category'

urlpatterns = [
    url('causes/', views.causes, name="causes"),
    url('charity1/', views.charity1, name="charity1"),
    url('charity2/', views.charity2, name="charity2"),
    url('charity3/', views.charity3, name="charity3"),
    url('charity4/', views.charity4, name="charity4"),
    url('charity5/', views.charity5, name="charity5"),
    url('charity6/', views.charity6, name="charity6"),
 ]


