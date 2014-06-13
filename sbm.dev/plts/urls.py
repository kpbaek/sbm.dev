from django.conf.urls import patterns, include, url
from plts.viewfolder import views, util_views, part_report_views, part_reject_views, shipment_views
from tastypie.api import Api
from plts.api import *

v1_api = Api(api_name='v1')
v1_api.register(ProductModelResource())
v1_api.register(ProductStatusResource())
v1_api.register(CompanyResource())
v1_api.register(WorkerResource())
v1_api.register(ProductResource())
v1_api.register(PartClassResource())
v1_api.register(PartTypeResource())
v1_api.register(PartResource())
v1_api.register(ManufacturingTypeResource())
v1_api.register(RepairErrorTypeResource())
v1_api.register(ManufacturingHistoryResource())
v1_api.register(PartHistoryResource())
v1_api.register(ShipmentHistoryResource())

urlpatterns = patterns('',
	url(r'^api/', include(v1_api.urls)),
	#url(r'^$', views.index, name='index'),
	url(r'^alert_then_back/(?P<message>[\w ]+)$', util_views.alert_then_back, name='alert_then_back'),
	
	# views for reporting parts
	url(r'^part/report/$', part_report_views.report_part_receiving, name='report_part_receiving'),
	url(r'^part/report/save/$', part_report_views.save_part_receiving, name='save_part_receiving'),
	url(r'^part/reject/$', part_reject_views.reject_part, name='reject_part'),
	url(r'^part/reject/save/$', part_reject_views.save_part_rejection, name='save_part_rejection'),
	

	url(r'^upload_manufacturing_history/$', views.upload_manufacturing_history, name='upload_manufacturing_history'),
	url(r'^upload_manufacturing_history/bulk_production/$', views.bulk_production, name='bulk_production'),
	url(r'^report_shipment/$', shipment_views.report_shipment, name='report_shipment'),
)
