from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from . import forms
# Create your views here.

def user(request):
    form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(request.POST)

        if form.is_valid():
            print("Validation Success")
            form.save(commit=True)

    return render(request,'AppTwo/user.html',{'form':form})
