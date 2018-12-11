from django.shortcuts import render, HttpResponse, redirect

def index(request):
    initial={'name': request.session.get('name', None)}
    form = (request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            return render(request, 'survey_form/index.html')
    return render(request, 'survey_form/index.html', {'form': form})

def submit(request):
	request.session['name']=request.POST['name']
	request.session['location']=request.POST['location']
	request.session['language']=request.POST['language']
	return redirect('/results')

def results(request):
	
	return render(request, 'survey_form/results.html')

# Create your views here.
