from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from plts.models import *
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.core.urlresolvers import reverse
from plts.digitChecker import *
invalid_barcode_message = "invalid_barcode2"

# views
def report_part_receiving(request):
	return render(request, 'plts/report_part_receiving.html', None)

# database updates
transaction.commit_manually
def save_part_receiving(request):
	raw_text = request.POST.get("raw_text")
	report_type = request.POST.get("report_type")
	part_sets = raw_text.split(",")

	for part_set in part_sets:
		if ":" in part_set:
			part_range = part_set.split(":")
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
			while barcode_base <= part_end:
				print "barcode_base = " + str(barcode_base)
				part = str(barcode_base) + str(getCheckDigit(barcode_base))
				print "check_digit = " + str(getCheckDigit(barcode_base))
				save_or_delete_part(part, report_type)
				barcode_base += 1
			
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
	print "in save_or_delete_part with part_barcode = " + part_barcode
	part_class_id = int(part_barcode[1:3])
	part_version = int(part_barcode[3:5])
	company_id = int(part_barcode[5:7])
	part_class = PartClass.objects.get(id=part_class_id)
	part_type = PartType.objects.get(part_class=part_class_id, version=part_version, company=company_id)
	
	if report_type == "save":
		part = Part.objects.create(barcode=part_barcode, part_type=part_type)
	
	elif report_type == "delete":
		#part_type = PartType.objects.get(part_class=part_class_id, version=part_version, company=company_id)
		part = Part.objects.filter(barcode=part_barcode, part_type=part_type)
		if part:
			part.delete()

def is_valid_barcode(barcode, barcode_type):
	if barcode_type is "part":
		if len(barcode) == 13:
			if barcode[0] == '1':
				return True

	return False



