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

class charity_list(models.Model):
    ch_id = models.AutoField(primary_key=True)
    ch_type = models.CharField(max_length=50)
    ch_intro = models.TextField(max_length=500)
    ch_about= models.TextField(max_length=500)
    ch_address= models.TextField(max_length=500)
    ch_contact= models.CharField(max_length=10)
    causes_id= models.ForeignKey(Causes, on_delete=models.CASCADE)
    ch_email= models.CharField(max_length=50)
    ch_license= models.CharField(max_length=50)
    img = models.ImageField(blank=True)
