from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Provider(models.Model):
    fantasy_name = models.CharField(max_length=100)
    tax_name = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=10)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.fantasy_name


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    from_date = models.DateTimeField(default=timezone.now)
    thru_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.name + ' (' + self.provider.fantasy_name + ')'

    
class Address(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    
    def __str__(self):
        return self.address1 + ' ' + self.address1 + ', ' + self.city + ', ' + self.country + ' (' + self.type + ', ' + self.provider.fantasy_name + ')'

    
class Contact(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
        
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + self.type + ', ' + self.provider.fantasy_name + ')'
