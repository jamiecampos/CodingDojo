from django.shortcuts import HttpResponse, render, redirect

# Create your views here.
def index(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 0
    return render(request, 'surveyform/index.html')

def process(request):
    if 'attempt' in request.session:
        request.session['attempt'] +=1
        if request.method == "POST":
            request.session['name'] = request.POST['name']
            request.session['location'] = request.POST['location']
            request.session['language'] = request.POST['language']
            request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    return render(request, 'surveyform/result.html')
