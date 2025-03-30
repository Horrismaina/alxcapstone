from django.db import models
from django.contrib.auth.models import User  # Using Django's built-in User model

# Category model to categorize products
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Product model to store product information
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # If category is deleted, delete related products
    stock_quantity = models.PositiveIntegerField()  # Ensuring stock quantity is positive
    image_url = models.URLField(max_length=200, blank=True, null=True)  # Optional image URL
    created_date = models.DateTimeField(auto_now_add=True)  # Automatically set when created

    def __str__(self):
        return self.name

