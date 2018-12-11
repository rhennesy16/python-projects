from django.shortcuts import render,redirect
from .models import Shows
from django.contrib import messages
# Create your views here.
def index(request):
	all_shows = {
		'shows':Shows.objects.all().values()
	}
	return render(request,'first_app/show.html', all_shows)

def process1(request):
	return render(request,'first_app/create.html')

def add(request):
	print(request.POST['title'])
	errors = Shows.objects.basic_validator(request.POST)
	if len(errors) > 0:
	# 	# if the errors dictionary contains anything, loop through each key-value pair and make a flash message
		for key, value in errors.items():
			messages.error(request, value)
	# 	# redirect the user back to the form to fix the errors
		return redirect('/add_new_show')
	else:
		# if the errors object is empty, that means there were no errors!
		# retrieve the blog to be updated, make the changes, and save
		show = Shows.objects.create(title=request.POST['title'],network=request.POST['network'],date=request.POST['date'])
		show.title = request.POST['title']
		show.save()
	messages.success(request, "Show successfully updated")
	return redirect('/')

def edit(request,number):
	context = {
	'show':Shows.objects.get(id=number)
	}
	return render(request,'first_app/update.html', context)

def process2(request,number):
	b=Shows.objects.get(id=number)
	b.title=request.POST["title"] 
	b.network=request.POST["network"]
	b.date=request.POST["date"]
	b.save()
	return redirect('/')

def destroy(request,number):
	delete = {
	'show':Shows.objects.get(id=number).delete()
	}
	return redirect('/')

def update(request, id):
	# pass the post data to the method we wrote and save the response in a variable called errors
	errors = Shows.objects.basic_validator(request.POST)
		# check if the errors dictionary has anything in it
	if len(errors) > 0:
		# if the errors dictionary contains anything, loop through each key-value pair and make a flash message
		for key, value in errors.items():
			messages.error(request, value)
		# redirect the user back to the form to fix the errors
		return redirect('/first_app/edit/'+id)
	else:
		# if the errors object is empty, that means there were no errors!
		# retrieve the blog to be updated, make the changes, and save
		show = Shows.objects.get(id = id)
		show.title = request.POST['title']
		show.save()
		messages.success(request, "Show successfully updated")
		# redirect to a success route
		return redirect('/')