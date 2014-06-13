from django.http import HttpResponse
from plts.models import *
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def report_shipment(request):
	try:
		print request.POST
		data = request.POST.get('data')
		data = json.loads(data)
		
		product_barcode = data['product_barcode']
		shipment_barcode = data['shipment_barcode']
		worker_barcode = data['worker_barcode']
		enterpriser = data['enterpriser']
		etc = data['etc']

		product = Product.objects.get(barcode=product_barcode)
		worker = Worker.objects.get(barcode=worker_barcode)
		
		shipmentHistory = ShipmentHistory.objects.create(
			product=product,
			shipment=shipment_barcode,
			worker=worker,
			enterprise=enterpriser,
			etc=etc
		)
		
		return HttpResponse("success")
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
		return HttpResponse(e.message)
