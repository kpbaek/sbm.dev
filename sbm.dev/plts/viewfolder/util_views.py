from django.shortcuts import render

def alert_then_back(request, message):
	return render(request, 'plts/alert_then_back.html', {'message': message})


