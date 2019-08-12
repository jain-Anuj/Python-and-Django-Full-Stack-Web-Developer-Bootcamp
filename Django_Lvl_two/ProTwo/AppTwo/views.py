from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
# Create your views here.

def user(request):
    user_details = User.objects.order_by('first_name')
    user_dict ={'user_records' : user_details}
    return render(request, 'AppTwo/user.html', context = user_dict)
