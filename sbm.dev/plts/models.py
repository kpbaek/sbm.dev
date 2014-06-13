from django.db import models

# Create your models here.

class ProductModel(models.Model):
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class ProductStatus(models.Model):
    priority = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class Company(models.Model):
    priority = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

class Worker(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=20)
    barcode = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name + " (" + self.barcode + ")"

class Product(models.Model):
    product_model = models.ForeignKey(ProductModel)
    barcode = models.CharField(max_length=20)
    product_status = models.ForeignKey(ProductStatus)
    reg_date = models.DateTimeField('date registered', auto_now=True)
    def __unicode__(self):
        return self.product_model.name + " (" + self.barcode + ")"

class PartClass(models.Model):
    priority = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class PartType(models.Model):
    product_model = models.ForeignKey(ProductModel)
    part_class = models.ForeignKey(PartClass)
    version = models.IntegerField()
    company = models.ForeignKey(Company)
    name = models.CharField(max_length=50)
    reg_date = models.DateTimeField('date registered', auto_now=True)
    def __unicode__(self):
        return self.name

class Part(models.Model):
    part_type = models.ForeignKey(PartType)
    barcode = models.CharField(max_length=20)
    reg_date = models.DateTimeField('date registered', blank=True, null=True)
    def __unicode__(self):
        return self.part_type.name + " (" + self.barcode + ")"

class ManufacturingType(models.Model):
    priority = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name
    
class RepairErrorType(models.Model):
    priority = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.name

class ManufacturingHistory(models.Model):
    manufacturing_type = models.ForeignKey(ManufacturingType)
    product = models.ForeignKey(Product)
    part = models.ForeignKey(Part)
    repair_error_type = models.ForeignKey(RepairErrorType, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=False)
    worker = models.ForeignKey(Worker)
    reg_date = models.DateTimeField('date registered', auto_now=True)
    def __unicode__(self):
        productInfo = self.product.product_model.name + " (" + self.product.barcode + ")"
        partInfo = self.part.part_type.name + " (" + self.part.barcode + ")"
        return productInfo + " <-> " + partInfo

class PartHistory(models.Model):
    part = models.ForeignKey(Part)
    remark = models.CharField(max_length=200, blank=True, null=True)
    worker = models.ForeignKey(Worker, default=12)
    reg_date = models.DateTimeField('date registered', auto_now=True)
    def __unicode__(self):
        return self.part.part_type.name + " (" + self.part.barcode + ")"

class ShipmentHistory(models.Model):
    product = models.ForeignKey(Product)
    shipment = models.CharField(max_length=20)
    worker = models.ForeignKey(Worker, default=12)
    enterprise = models.CharField(max_length=200)
    etc = models.CharField(max_length=200, blank=True, null=True)
    reg_date = models.DateTimeField('date registered', auto_now=True)
    def __unicode__(self):
        return self.product.product_model.name + " (" +self.shipment + ")"
    
