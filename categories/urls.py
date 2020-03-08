from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views


app_name='category'

urlpatterns = [
    url('causes/', views.causes, name="causes"),



]