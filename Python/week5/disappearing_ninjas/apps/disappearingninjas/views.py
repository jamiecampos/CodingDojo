from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'disappearingninjas/index.html')

def ninjas(request):
    return render (request, 'disappearingninjas/ninjas.html')

def color(request, color):
    context = {'color' : color,}
    if color == 'blue':
        context['name'] = 'disappearingninjas/images/leonardo.jpg'
    elif color == 'orange':
        context['name'] = 'disappearingninjas/images/michelangelo.jpg'
    elif color == 'red':
        context['name'] = 'disappearingninjas/images/raphael.jpg'
    elif color == 'purple':
        context['name'] = 'disappearingninjas/images/donatello.jpg'
    else:
        context['name'] = 'disappearingninjas/images/notapril.jpg'
    return render (request, 'disappearingninjas/color.html', context)
