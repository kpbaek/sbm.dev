from django.contrib import admin
from plts.models import *

# Register your models here

class ManufacturingHistoryAdmin(admin.ModelAdmin):
    list_display = ('manufacturing_type','product','part','worker', 'reg_date')
    list_filter = ['reg_date', 'manufacturing_type', 'product__product_model', 'part__part_type','worker' ]
    search_fields = ['product__barcode', 'part__barcode', 'worker__barcode', 'worker__name']

class PartHistoryAdmin(admin.ModelAdmin) :
    list_display = ('part','remark', 'worker', 'reg_date')
    list_filter = ['reg_date', 'part__part_type', 'worker']

class ShipmentHistoryAdmin(admin.ModelAdmin) :
    list_display = ('product', 'shipment', 'worker', 'enterprise', 'etc', 'reg_date')
    list_filter = ['reg_date', 'product__product_model', 'worker', 'enterprise']

class PartAdmin(admin.ModelAdmin):
    search_fields = ['barcode']

admin.site.register(ProductModel)
admin.site.register(ProductStatus)
admin.site.register(Company)
admin.site.register(Worker)

admin.site.register(Product)
admin.site.register(PartClass)
admin.site.register(PartType)
admin.site.register(Part, PartAdmin)

admin.site.register(ManufacturingType)
admin.site.register(RepairErrorType)
admin.site.register(ManufacturingHistory, ManufacturingHistoryAdmin)
admin.site.register(PartHistory, PartHistoryAdmin)
admin.site.register(ShipmentHistory, ShipmentHistoryAdmin)
