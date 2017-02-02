from django.shortcuts import render, redirect, HttpResponse
import datetime
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session and 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, 'ninjagold/index.html')

def process(request, location):
    time_now = datetime.datetime.now().strftime("%m/%d/%Y %I:%M %p")

    if location == 'farm':
        random_num = random.randrange(10,21)
        request.session['gold'] += random_num
        summary = "Earned " + str(random_num) + " golds from the farm! " + "(" + str(time_now) + ")"
        request.session['activities'].append(summary)
    elif location == 'cave':
        random_num = random.randrange(5,11)
        request.session['gold'] += random_num
        summary = "Earned " + str(random_num) + " golds from the cave! " + "(" + str(time_now) + ")"
        request.session['activities'].append(summary)
    elif location == 'house':
        random_num = random.randrange(2,6)
        request.session['gold'] += random_num
        summary = "Earned " + str(random_num) + " golds from the house! " + "(" + str(time_now) + ")"
        request.session['activities'].append(summary)
    elif location == 'casino':
        random_num = random.randrange(-50,51)
        request.session['gold'] += random_num
        if random_num > 0:
            summary = "Entered a casino and won " + str(random_num) + " golds! " + "(" + str(time_now) + ")"
            request.session['activities'].append(summary)
        elif random_num < 0:
            summary = "Entered a casino and lost " + str(random_num) + " golds... Ouch.. " + "(" + str(time_now) + ")"
            request.session['activities'].append(summary)
        else:
            summary = "Entered a casino and broke even. " + "(" + str(time_now) + ")"
            request.session['activities'].append(summary)
    else:
        return redirect('/')

    return redirect('/')
