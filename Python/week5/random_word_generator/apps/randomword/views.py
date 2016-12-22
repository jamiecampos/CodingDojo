from django.shortcuts import HttpResponse, render, redirect
import random, string

# Create your views here.
def index(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 0
        request.session['random_string'] = 'GENERATE A RANDOM WORD'
    return render(request, "randomword/index.html")

def randomize(request):
    random_string = ''.join(random.choice(string.uppercase) for i in range(15))
    request.session['attempt'] += 1
    request.session['random_string'] = random_string
    return redirect('/')
