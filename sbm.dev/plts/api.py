from django.db.models import Q
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from plts.models import *
from plts.serializer import MySerializer

class ProductModelResource(ModelResource):
	class Meta:
		queryset = ProductModel.objects.all()
		resource_name = 'product_model'
		filtering = {
			'id': ALL,
			'name': ALL,
			'barcode_prefix': ALL
		}

class ProductStatusResource(ModelResource):
	class Meta:
		queryset = ProductStatus.objects.all().order_by('priority')
		resource_name = 'product_status'
		filtering = {
			'name': ALL
		}
		ordering = {
			'priority'
		}

class CompanyResource(ModelResource):
	class Meta:
		queryset = Company.objects.all().order_by('priority')
		resource_name = 'company'
		filtering = {
			'id': ALL,
			'name': ALL
		}

class WorkerResource(ModelResource):
	company = fields.ForeignKey(CompanyResource, 'company', full=True)

	class Meta:
		queryset = Worker.objects.all()
		resource_name = 'worker'
		filtering = {
			'id': ALL,
			'company': ALL_WITH_RELATIONS,
			'name': ALL,
			'barcode': ALL
		}
		
	
	

class ProductResource(ModelResource):
	product_model = fields.ForeignKey(ProductModelResource, 'product_model', full=True)
	product_status = fields.ForeignKey(ProductStatusResource, 'product_status', full=True)

	class Meta:
		queryset = Product.objects.all()
		resource_name = 'product'
		filtering = {
			'id': ALL,
			'product_model': ALL_WITH_RELATIONS,
			'barcode': ALL,
			'product_status': ALL_WITH_RELATIONS,
			'reg_date': ALL
		}

class PartClassResource(ModelResource):
	class Meta:
		queryset = PartClass.objects.all().order_by('priority')
		resource_name = 'part_class'
		filtering = {
			'id': ALL,
			'name': ALL
		}

class PartTypeResource(ModelResource):
	product_model = fields.ForeignKey(ProductModelResource, 'product_model', full=True)
	part_class = fields.ForeignKey(PartClassResource, 'part_class', full=True)
	company = fields.ForeignKey(CompanyResource, 'company', full=True)

	class Meta:
		queryset = PartType.objects.all()
		resource_name = 'part_type'
		filtering = {
			'id': ALL,
			'product_model': ALL_WITH_RELATIONS,
			'part_class': ALL_WITH_RELATIONS,
			'version': ALL,
			'company': ALL_WITH_RELATIONS,
			'name': ALL,
			'reg_date': ALL
		}

class PartResource(ModelResource):
	part_type = fields.ForeignKey(PartTypeResource, 'part_type', full=True)

	class Meta:
		queryset = Part.objects.all();
		resource_name = 'part'
		filtering = {
			'id': ALL,
			'part_type': ALL_WITH_RELATIONS,
			'barcode': ALL,
			'reg_date': ALL
		}

class ManufacturingTypeResource(ModelResource):
	class Meta:
		queryset = ManufacturingType.objects.all().order_by('priority')
		resource_name = 'manufacturing_type'
		filtering = {
			'id': ALL,
			'name': ALL
		}

class RepairErrorTypeResource(ModelResource):
	class Meta:
		queryset = RepairErrorType.objects.all().order_by('priority')
		resource_name = 'repair_error_type'
		filtering = {
			'id': ALL,
			'name': ALL
		}

class ManufacturingHistoryResource(ModelResource):
	manufacturing_type = fields.ForeignKey(ManufacturingTypeResource, 'manufacturing_type', full=True)
	product = fields.ForeignKey(ProductResource, 'product', full=True)
	part = fields.ForeignKey(PartResource, 'part', full=True)
	repair_error_type = fields.ForeignKey(RepairErrorTypeResource, 'repair_error_type', full=True, null=True)
	worker = fields.ForeignKey(WorkerResource, 'worker', full=True)

	class Meta:
		queryset = ManufacturingHistory.objects.all();
		resource_name = 'manufacturing_history'
		serializer = MySerializer()
		filtering = {
			'id': ALL,
			'manufacturing_type': ALL_WITH_RELATIONS,
			'product': ALL_WITH_RELATIONS,
			'part': ALL_WITH_RELATIONS,
			'repair_error_type': ALL_WITH_RELATIONS,
			'remark': ALL,
			'worker': ALL_WITH_RELATIONS,
			'reg_date': ALL,
			'manufacturing_type_name': ['exact',],
		}

	
	def build_filters(self, filters=None):
		if filters is None:
			filters = {}
		orm_filters = super(ManufacturingHistoryResource, self).build_filters(filters)

		if('manufacturing_type_name' in filters):
			value = filters['manufacturing_type_name']
			type_list = value.split(",")
			
			qset = None
			for type_name in type_list:
				qobj = Q(manufacturing_type__name__exact=type_name)
				qset = qset | qobj if qset else qobj
			
			orm_filters.update({'custom': qset})

		return orm_filters
	
	def apply_filters(self, request, applicable_filters):
		if 'custom' in applicable_filters:
			custom = applicable_filters.pop('custom')
		else:
			custom = None

		semi_filtered = super(ManufacturingHistoryResource, self).apply_filters(request, applicable_filters)
		return semi_filtered.filter(custom) if custom else semi_filtered
		
class PartHistoryResource(ModelResource):
	part = fields.ForeignKey(PartResource, 'part', full=True)
	worker = fields.ForeignKey(WorkerResource, 'worker', full=True)

	class Meta:
		queryset = PartHistory.objects.all()
		resource_name = 'part_history'
		serializer = MySerializer()
		filtering = {
			'id': ALL,
			'part': ALL_WITH_RELATIONS,
			'worker': ALL_WITH_RELATIONS,
		}
		
class ShipmentHistoryResource(ModelResource):
	product = fields.ForeignKey(ProductResource, 'product', full=True)
	worker = fields.ForeignKey(WorkerResource, 'worker', full=True)

	class Meta:
		queryset = ShipmentHistory.objects.all()
		resource_name = 'shipment_history'
		filtering = {
				'id': ALL,
				'shipment' : ALL,
				'product': ALL_WITH_RELATIONS,
				'worker' : ALL_WITH_RELATIONS,
				'enterprise' : ALL,
				'etc' : ALL
		}
