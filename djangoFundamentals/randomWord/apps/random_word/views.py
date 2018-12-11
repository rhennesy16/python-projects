from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
	context = {
		'rstring': get_random_string(length=5)
	}
	if 'count' in request.session:
		request.session['count']=request.session['count'] +1
	else:
		request.session['count'] = 1
	return render(request,'random_word/index.html', context)
# Create your views here.
