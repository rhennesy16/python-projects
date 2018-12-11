from django.shortcuts import render,redirect,HttpResponse
from .models import Shows
# Create your views here.
def index(request):
	"""show initial page with all TV shows"""
	all_shows = {
	'shows': Shows.objects.all().values()
	}
	return render(request, 'semi_restful/all.html', all_shows)

def new(request):
	"""show page with form to add TV shows"""
	return render(request, 'semi_restful/add.html')

def add(request):
	Shows.objects.create(title=request.POST["title"], network=request.POST["network"], date=request.POST["date"])
	return redirect('/')

def edit(request,number):
	context = {
		'show':Shows.objects.get(id=number)
	}
	return render(request, 'semi_restful/edit.html', context)

def append(request,number):
	b=Shows.objects.get(id=number)
	b.title=request.POST["title"] 
	b.network=request.POST["network"]
	b.date=request.POST["date"]
	b.save()
	return redirect('/')

def destroy(request,number):
	context = {
		'show':Shows.objects.get(id=number).delete()
	}
	return redirect('/')
