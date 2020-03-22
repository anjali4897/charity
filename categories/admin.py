from django.contrib import admin
from .models import Category,Causes,charity_list
# Register your models here.

admin.site.register(Category)
admin.site.register(Causes)
admin.site.register(charity_list)