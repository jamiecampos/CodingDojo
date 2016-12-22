from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
    date_now = datetime.datetime.now().date()
    time_now = datetime.datetime.now().time()
    date_time = {
    'date': date_now,
    'time': time_now
    }
    return render(request, "timedisplay/index.html", date_time)
