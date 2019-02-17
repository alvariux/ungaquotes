from django.db import models
from django.utils import timezone

class Business(models.Model):
    name = models.CharField(max_length=200,blank=False, null=False)
    tax_id = models.CharField(max_length=20,blank=True, null=True)
    address = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    state = models.CharField(max_length=200,blank=True, null=True)
    zipcode = models.CharField(max_length=10,blank=True, null=True)
    phone = models.CharField(max_length=200,blank=True, null=True)
    web = models.CharField(max_length=200,blank=True, null=True)
    fax = models.CharField(max_length=200,blank=True, null=True)
    email = models.EmailField(max_length=200,blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']