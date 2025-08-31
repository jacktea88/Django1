#-*- coding: utf-8 -*-
from django.db import models
from filer.fields.image import FilerImageField

class Poll(models.Model):
    name = models.CharField(max_length=200, null=False)
    created_at = models.DateField(auto_now_add=True)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class PollItem(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=False)
    image_url = models.CharField(max_length=200, null=True, blank=True)
    vote = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class VoteCheck(models.Model):
    userid = models.PositiveIntegerField()
    pollid = models.PositiveIntegerField()
    vote_date = models.DateField()

class Category(models.Model):
    name = models.CharField( max_length=200)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey( Category, on_delete=models.CASCADE)
    sku = models.CharField( max_length=50)
    name = models.CharField( max_length=50)
    description = models.TextField()
    # image = models.URLField(max_length=200, null=True)
    image = FilerImageField(related_name='product_image', null=True, on_delete=models.SET_NULL)
    website = models.URLField(max_length=200, null=True)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

