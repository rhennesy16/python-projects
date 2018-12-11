from django.shortcuts import render,redirect
from .models import Users, Messages, Comments
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
	return redirect('/welcome')

def welcome(request):
	context = {
		'messages':Messages.objects.all()
	}
	return render(request,'login/wall.html',context)

def message(request):
	current_user = Users.objects.get(id=request.session['user_id'])
	Messages.objects.create(message=request.POST['message'],user=current_user)
	return redirect('/welcome')

def comment(request):
	current_user = Users.objects.get(id=request.session['user_id'])
	current_message = Messages.objects.get(id=request.POST['message_id'])
	Comments.objects.create(comment=request.POST['comment'],user=current_user, message=current_message)
	return redirect('/welcome')

def login(request):
	errors = Users.objects.login_validator(request.POST)
	if len(errors):
		for key, value in errors.items():
			messages.error(request, value)
		return redirect('/')
	user = Users.objects.filter(email=request.POST['email'])
	request.session['user_id'] = user[0].id
	print("logging in!")
	return redirect('/welcome')

def logout(request):
	request.session.clear()
	print('bye')
	return redirect('/')
