from django.db import models
from django.contrib import admin
# Create your models here.
class Product(models.Model):
    Product_name = models.CharField(max_length=20, help_text="Enter Prod Name")
    Prod_ID = models.IntegerField(help_text="Enter Prod_id")
    Prod_no = models.IntegerField(help_text="Enter the Product Number")

class ProductAdmin(admin.ModelAdmin):
    list_display = ['Product_name', 'Prod_ID', 'Prod_no']
