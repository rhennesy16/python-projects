from django.shortcuts import render,redirect
from .models import Logins
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
	try:
		if request.session['loggedin'] == True:
			return redirect('/welcome')
	except:
		pass		 
	return render(request,'login/register.html')

def register(request):
	errors = Logins.objects.basic_validator(request.POST)
	if len(errors) > 0:
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	else:
		hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
		Logins.objects.create(first_name=request.POST['first_name'],email=request.POST['email'],password=hash1.decode())
	request.session['loggedin'] = True
	print(login)
	return redirect('/welcome')

def welcome(request):
	return render(request,'login/welcome.html')

def login(request):
	try:
		user = Logins.objects.get(email=request.POST['email'])		# is it really a good idea to use get here?	
		if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
			request.session['loggedin'] = True
			return redirect('/welcome')
	except:
		return redirect('/')

def logout(request):
	request.session.clear()
	return redirect('/')
