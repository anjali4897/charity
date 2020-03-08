from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [


     url('signup/', views.signup_info, name="signup"),
     url('login/',views.login_info, name="login")

]