from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=200,blank=False, null=False)
    tax_id = models.CharField(max_length=20,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    state = models.CharField(max_length=200,blank=True, null=True)
    zipcode = models.CharField(max_length=10,blank=True, null=True)
    phone = models.CharField(max_length=200,blank=True, null=True)
    web = models.CharField(max_length=200,blank=True, null=True)
    fax = models.CharField(max_length=200,blank=True, null=True)
    email = models.CharField(max_length=200,blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Contact(models.Model):
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    name = models.CharField(max_length=200,blank=False, null=False)    
    phone = models.CharField(max_length=200,blank=True, null=True)
    mobile = models.CharField(max_length=200,blank=True, null=True)    
    email = models.CharField(max_length=200,blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
