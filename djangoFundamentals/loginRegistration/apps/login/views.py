from django.shortcuts import render,redirect
from .models import Users,Chores
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
	try:
		if request.session['loggedin'] == True:
			return redirect('/jobs')
	except:
		pass		 
	return render(request,'login/register.html')

def register(request):
	errors = Users.objects.registration_validator(request.POST)
	if len(errors): 
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		x = Users.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=hash1)
		print(x)
		request.session['loggedin'] = True
		request.session['user_id'] = x.id
	print('hello')
	return redirect('/jobs')

def login(request):
	errors = Users.objects.login_validator(request.POST)
	if len(errors):
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	user = Users.objects.filter(email=request.POST['email'])
	request.session['user_id'] = user[0].id
	print("logging in!")
	return redirect('/jobs')

def jobs(request):
	"""show initial page with all TV shows"""
	all_jobs = {
	'chores': Chores.objects.all().values()
	}
	return render(request, 'login/jobs.html', all_jobs)

def new(request):
	"""show page with form to add TV shows"""
	return render(request, 'login/newjob.html')

def add(request):
	errors = Chores.objects.job_validator(request.POST)
	if len(errors):
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/new')
	current_user = Users.objects.get(id=request.session['user_id'])
	Chores.objects.create(user=current_user, title=request.POST["title"], description=request.POST["description"], location=request.POST["location"])
	return redirect('/jobs')

def show(request,number):
	context = {
		'chores': Chores.objects.get(id=number)
		}
	return render(request,'login/show.html', context)

def edit(request,number):
	context = {
		'chores':Chores.objects.get(id=number)
	}
	return render(request, 'login/edit.html', context)

def append(request,number):
	errors = Chores.objects.job_validator(request.POST)
	if len(errors):
		for key, value in errors.items():
			messages.error(request, value)
		return redirect(f'/edit/{number}')
	current_user = Users.objects.get(id=request.session['user_id'])
	job=Chores.objects.get(id=number)
	job.title=request.POST["title"]
	job.description=request.POST["description"] 
	job.location=request.POST["location"]
	job.save()
	return redirect('/jobs')

def destroy(request,number):
	context = {
		'chore':Chores.objects.get(id=number).delete()
	}
	return redirect('/jobs')

def logout(request):
	request.session.clear()
	print('bye')
	return redirect('/')

