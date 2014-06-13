from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from plts.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.core.urlresolvers import reverse

import json

invalid_barcode_message = "invalid_barcode"

# views
def report_part_receiving(request):
	return render(request, 'plts/report_part_receiving.html', None)

def reject_part(request):
	return render(request, 'plts/reject_part.html', None)

def alert_then_back(request, message):
	return render(request, 'plts/alert_then_back.html', {'message': message})

# database updates
transaction.commit_manually
def save_part_receiving(request):
	raw_text = request.POST.get("raw_text")
	report_type = request.POST.get("report_type")

	part_sets = raw_text.split(",")
	for part_set in part_sets:
		if ":" in part_set:
			part_range = part_set.split("~")
			if not is_valid_barcode(part_range[0].strip(), "part"):
				transaction.rollback()
				return HttpResponseRedirect(reverse('plts:alert_then_back', args=(invalid_barcode_message, )))
			if not is_valid_barcode(part_range[1].strip(), "part"):
				transaction.rollback()
				return HttpResponseRedirect(reverse('plts:alert_then_back', args=(invalid_barcode_message, )))
				
			part_start = int((part_range[0].strip())[:12])
			part_end = int((part_range[1].strip())[:12])

			print "part_start = " + str(part_start)
			print "part_end = " + str(part_end)
			
			barcode_base = part_start
			while barcode_base != part_end:
				part = str(barcode_base) + str(getCheckDigit(barcode_base))
				save_or_delete_part(part, report_type)
				barcode_base += 1
			
			for barcode_base in range(part_start, part_end + 1):
				part = str(barcode_base * 10)
				save_or_delete_part(part, report_type)
			
		else:
			part = part_set.strip()
			if not is_valid_barcode(part, "part"):
				transaction.rollback()
				return HttpResponseRedirect(reverse('plts:alert_then_back', args=(invalid_barcode_message, )))
			save_or_delete_part(part, report_type)
	
	transaction.commit()
	return HttpResponseRedirect(reverse('plts:report_part_receiving'))

def save_or_delete_part(part_barcode, report_type):
	part_barcode = part_barcode.strip()
	#get part type
	print part_barcode
	part_class_id = int(part_barcode[1:3])
	part_version = int(part_barcode[3:5])
	company_id = int(part_barcode[5:7])
	part_class = PartClass.objects.get(id=part_class_id)
	part_type = PartType.objects.get(part_class=part_class_id, version=part_version, company=company_id)
	
	if report_type is "save":
		part = 1
		part = Part.objects.create(barcode=part_barcode, part_type=part_type)
	
	elif report_type is "delete":
		part = 2
		part = Part.objects.delete(barcode=part_barcode, part_type=part_type)

def is_valid_barcode(barcode, barcode_type):
	print barcode
	if barcode_type is "part":
		if len(barcode) == 13:
			if barcode[0] == '1':
				return True

	return False

def save_part_rejection(request):
	return HttpResponseRedirect(reverse('plts:report_part_rejection'))

@transaction.commit_manually
@csrf_exempt
def upload_manufacturing_history(request):
	try:
		print request.POST
		data = request.POST.get('data')
		print data
		data = json.loads(data)
		
		manufacturing_type_name = data['manufacturing_type_name']
		product_barcode = data['product_barcode']
		part_barcode = data['part_barcode']
		worker_barcode = data['worker_barcode']
		repair_error_type_id_str = data['repair_error_type']
		remark = data['remark']
		
		#get product
		product_model_id = int(product_barcode[1:3])
		product_model = ProductModel.objects.get(id=product_model_id)
		product_status = ProductStatus.objects.get(id=1)
		product, product_created = Product.objects.get_or_create(barcode=product_barcode, product_model=product_model, defaults={'product_status':product_status})
	
		#get worker
		worker = Worker.objects.get(barcode=worker_barcode)
		
		#get part
		part_class_id = int(part_barcode[1:3])
		part_version = int(part_barcode[3:5])
		company_id = int(part_barcode[5:7])
		part_class = PartClass.objects.get(id=part_class_id)
		part_type = PartType.objects.get(part_class=part_class_id, version=part_version, company=company_id)
		part, part_created = Part.objects.get_or_create(barcode=part_barcode, part_type=part_type)

		#create manufacturing history
		manufacturing_type = ManufacturingType.objects.get(name=manufacturing_type_name)
		
		if(repair_error_type_id_str != ""):
			repair_error_type_id = int(repair_error_type_id_str)
			repair_error_type = RepairErrorType.objects.get(id=repair_error_type_id)
		else:
			repair_error_type = None
	
		manufacturingHistory = ManufacturingHistory.objects.create(
			manufacturing_type=manufacturing_type,
			product=product,
			part=part,
			repair_error_type=repair_error_type,
			remark=remark,
			worker=worker
		)

		transaction.commit()
		return HttpResponse("success")
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
		transaction.rollback()
		return HttpResponse(e.message)


@transaction.commit_manually
@csrf_exempt
def bulk_production(request):
	try:
		print "bulk production"
		print request.POST
		data = request.POST.get('data')
		print data
		data = json.loads(data)
		
		manufacturing_type_name = data['manufacturing_type_name']
		product_barcode = data['product_barcode']
		part_barcode_list = data['part_barcode']
		worker_barcode = data['worker_barcode']
		repair_error_type_id_str = ""
		remark = ""
		
		#get product
		product_model_id = int(product_barcode[1:3])
		product_model = ProductModel.objects.get(id=product_model_id)
		product_status = ProductStatus.objects.get(id=1)
		product, product_created = Product.objects.get_or_create(barcode=product_barcode, product_model=product_model, defaults={'product_status':product_status})
		
		#get worker
		worker = Worker.objects.get(barcode=worker_barcode)
		manufacturing_type = ManufacturingType.objects.get(name=manufacturing_type_name)
		if(repair_error_type_id_str != ""):
			repair_error_type_id = int(repair_error_type_id_str)
			repair_error_type = RepairErrorType.objects.get(id=repair_error_type_id)
		else:
			repair_error_type = None
		
	
		for part_barcode in part_barcode_list:
			#get part
			part_class_id = int(part_barcode[1:3])
			part_version = int(part_barcode[3:5])
			company_id = int(part_barcode[5:7])
			part_class = PartClass.objects.get(id=part_class_id)
			part_type = PartType.objects.get(part_class=part_class_id, version=part_version, company=company_id)
			part, part_created = Part.objects.get_or_create(barcode=part_barcode, part_type=part_type)
	
			#create manufacturing history
			
			manufacturingHistory = ManufacturingHistory.objects.create(
				manufacturing_type=manufacturing_type,
				product=product,
				part=part,
				repair_error_type=repair_error_type,
				remark=remark,
				worker=worker
			)

		transaction.commit()
		return HttpResponse("success")
	except Exception as e:
		print '%s (%s)' % (e.message, type(e))
		transaction.rollback()
		return HttpResponse(e.message)

