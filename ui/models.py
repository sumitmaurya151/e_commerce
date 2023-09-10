from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_title = models.CharField(max_length=25)
    product_description = models.CharField(max_length=100)
    product_price = models.PositiveIntegerField()
    product_discount  = models.PositiveIntegerField()
    product_slug = models.CharField(max_length=200)
    product_pic =models.ImageField()


