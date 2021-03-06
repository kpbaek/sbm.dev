from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from plts.models import *
from django.core.urlresolvers import reverse

invalid_barcode_message = "invalid_barcode"

def reject_part(request):
	return render(request, 'plts/reject_part.html', None)

def save_part_rejection(request):
	invalid_barcode_response = HttpResponseRedirect(reverse('plts:alert_then_back', args=(invalid_barcode_message, )))
	part_barcode = request.POST.get("barcode")
	reject_reason = request.POST.get("reject_reason")

	print "part_barcode = " + part_barcode
	print "reject_reason = " + reject_reason.encode('utf-8')

	if part_barcode is None:
		print "part_barcode is none"
		return invalid_barcode_response

	parts = Part.objects.filter(barcode=part_barcode)
	
	print type(parts)
	if parts:
		part = parts[0]
		part_history = PartHistory.objects.create(part=part, remark=reject_reason)

	else:
		print "no matching part for part_barcode = " + part_barcode
		return invalid_barcode_response

	return HttpResponseRedirect(reverse('plts:reject_part'))
