from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hey There get lost!!")

def help(request):
    dict = {'var':'Help Page'}
    return render(request , 'AppTwo/help.html', context=dict)
