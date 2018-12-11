from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# Create your views here.
def index(request):
	context = {
		'time': strftime('%H:%M %p',gmtime()),
		'date': strftime('%Y-%m-%d',gmtime())
	}
	return render(request,'time_app/index.html', context)