from django.contrib import admin
from pos.models import *

class PurchaseInvoiceItemadmin(admin.ModelAdmin):
    list_display = ('invoice', 'product','quantity','price','cost_price')
    search_fields = ('invoice', 'product','quantity','price','cost_price')

class SaleInvoiceadmin(admin.ModelAdmin):
    list_display = ('customer','datetime')
    search_fields = ('customer','datetime')
	
class ItemsInline(admin.TabularInline):
	model = PurchaseInvoiceItem

class PurchaseInvoiceadmin(admin.ModelAdmin):
	inlines = [ItemsInline,]


admin.site.register(PurchaseInvoiceItem,PurchaseInvoiceItemadmin)
admin.site.register(PurchaseInvoice,PurchaseInvoiceadmin)
admin.site.register(PurchaseInvoice)
admin.site.register(SaleInvoice,SaleInvoiceadmin)
admin.site.register(Product)
admin.site.register(ProductPrice)
admin.site.register(Payment)
admin.site.register(CompanyContact)
admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Category)