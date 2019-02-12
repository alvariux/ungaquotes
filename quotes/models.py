from django.db import models
from django.utils import timezone

class Quote(models.Model):
    business = models.ForeignKey('business.Business', on_delete=models.CASCADE)
    client = models.ForeignKey('clients.Client', on_delete=models.CASCADE)
    contact = models.ForeignKey('clients.Contact', on_delete=models.CASCADE)
    status = models.PositiveIntegerField(default=0,blank=False,null=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%d - %s - %s - %s - %s' %(self.id,self.business.name,self.client.name,self.contact.name,self.created_date)

class QuoteDetail(models.Model):
    quote = models.ForeignKey('quotes.Quote', on_delete=models.CASCADE)
    unit = models.CharField(max_length=200,blank=False,null=False)
    quantity = models.IntegerField(blank=True, null=True)
    sku = models.CharField(max_length=200,blank=True, null=True)    
    description = models.TextField(blank=True, null=True)    
    unit_price = models.DecimalField(max_digits=12, decimal_places=2,blank=True, null=True)    
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%d - %s' %(self.id,self.quote)
