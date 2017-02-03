from django.shortcuts import render
from . import models
# Create your views here.
def index(req):
    users = models.Users.objects.all()
    context = {'users':users}
    return render(req, "friendapp/index.html",context)
