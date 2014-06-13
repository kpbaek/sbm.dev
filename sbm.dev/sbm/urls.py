from django.conf.urls import patterns, include, url
from django.contrib import admin

from sample_board import sampleViews 
from sample_board.api import EntryResource, UserResource

from tastypie.api import Api
from plts.api import *
from plts.viewfolder import views, util_views, part_report_views, part_reject_views, shipment_views

admin.autodiscover()

entry_resource = EntryResource()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())

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
    # Examples:
    # url(r'^$', 'sbm.sampleViews.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', sampleViews.home),
    url(r'^listSpecificPageWork/$', sampleViews.listSpecificPageWork),
    url(r'^searchWithSubject$', sampleViews.searchWithSubject),
    url(r'^listSearchedSpecificPageWork/$', sampleViews.listSearchedSpecificPageWork),
    url(r'^show_write_form/$', sampleViews.show_write_form),
    url(r'^DoWriteBoard$', sampleViews.DoWriteBoard),
    url(r'^viewWork/$', sampleViews.viewWork),
    url(r'^listSpecificPageWork_to_update/$', sampleViews.listSpecificPageWork_to_update),
    url(r'^updateBoard$', sampleViews.updateBoard),
    url(r'^DeleteSpecificRow/$', sampleViews.DeleteSpecificRow),
    
    
    
    
    url(r'^plts/', include('plts.urls', namespace='plts')),
    
    url(r'^apitest/', include(entry_resource.urls)),
    url(r'^api/', include(v1_api.urls)),    
    
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
