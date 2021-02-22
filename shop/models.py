from django.db import models


# Create your models here.
class category(models.Model):
    cat_name = models.CharField(max_length=20)


class Product(models.Model):
    p_name = models.CharField(max_length=20)
    p_cat = models.ForeignKey(to='shop.category', blank=True, null=True, on_delete=models.CASCADE)
    p_price = models.IntegerField()
    p_desc = models.CharField(max_length=200)
    p_img = models.ImageField(upload_to='img')


class cart(models.Model):
    p_user = models.CharField(max_length=20)
    p_name = models.CharField(max_length=20)
    p_price = models.IntegerField()
    p_qty = models.IntegerField()
    p_img = models.ImageField(upload_to='img')
    p_status = models.BooleanField(default=False)
    p_admin_status = models.BooleanField(default=False)


class contacts(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    sub = models.CharField(max_length=20)
    msg = models.CharField(max_length=200)
