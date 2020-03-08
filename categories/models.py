

# Create your models here.

from django.db import models

from django import forms

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)

class Causes(models.Model) :
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    img = models.ImageField(blank=True)

#class charity_list(models.Model):
