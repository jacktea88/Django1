from django.db import models
from django.contrib import auth
# for filer
from filer.fields.image import FilerImageField
# from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=False)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
# use profile model
class Profile(models.Model):
    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    height = models.PositiveIntegerField(default=160)
    male = models.BooleanField(default=False)
    website = models.URLField()

    def __str__(self):
        return self.user.username 

# vote model
class Vote(models.Model):
    name = models.CharField(max_length=20)
    no = models.IntegerField()
    sex = models.BooleanField(default=False)
    byear = models.IntegerField()
    party = models.CharField(max_length=20)
    votes = models.IntegerField()

    def __str__(self):
        return self.name

# 建立溫度紀錄資料表
class Temperature(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.temperature)    
    
# 建立產品分類資料表
class Category(models.Model):
    name = models.CharField(max_length=20)
    

    def __str__(self):
        return self.name

# 建立產品資料表
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.TextField()
    # image = models.URLField(null=True)
    # for filer
    image = FilerImageField(null=True, blank=True, related_name="product_image", on_delete=models.CASCADE)
    website = models.URLField(max_length=200, null=True)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name
    
# 建立訂單資料表
class Order(models.Model):
    user = models.ForeignKey(auth.models.User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return 'Order:{}'.format(self.id)
    
# 建立訂單明細資料表
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)