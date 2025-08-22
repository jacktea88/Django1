from django.db import models

# Create your models here.
class Vote(models.Model):
    name = models.CharField(max_length=20)
    no = models.IntegerField()
    sex = models.BooleanField(default=False)
    byear = models.IntegerField()
    party = models.CharField(max_length=20)
    votes = models.IntegerField()
    
    def __str__(self):
        return self.name
    