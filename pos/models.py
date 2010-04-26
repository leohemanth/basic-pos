from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    shortcut = models.CharField(max_length=100)

class ProductPrice(models.Model):
    product = models.ForeignKey(Product)
    selling_price = models.DecimalField(max_digits=7,decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-datetime']
    
class PurchaseInvoice(models.Model):
    company = models.ForeignKey('Company')
    datetime = models.DateTimeField()
    
class Payment(models.Model):
    mode_choices = ((1,'Cheque'),
                    (2,'Cash'),
                    (3,'DD'))
    mode = models.PositiveSmallIntegerField(choices=mode_choices)
    description = models.TextField()
    invoice = models.ForeignKey(PurchaseInvoice)
    
class PurchaseInvoiceItem(models.Model):
    invoice = models.ForeignKey(PurchaseInvoice)
    product = models.ForeignKey(Product)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=7,decimal_places=2)
    cost_price = models.DecimalField(max_digits=7,decimal_places=2)
    
class SaleInvoice(models.Model):
    customer = models.ForeignKey('Customer')
    datetime = models.DateTimeField(auto_now=True)
    
class SaleInvoiceItem(models.Model):
    invoice = models.ForeignKey(SaleInvoice)
    product = models.ForeignKey(Product)
    quantity = models.PositiveSmallIntegerField()
    sold_at_price = models.DecimalField(max_digits=7,decimal_places=2)
    
class CompanyContact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    description = models.TextField()
    company = models.ForeignKey('Company')
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    phone_number = models.CharField(max_length=11)
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    phone_number = models.CharField(max_length=11)
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product)
    
