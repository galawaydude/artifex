from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if(request.method == 'POST'):

        # getting the post parameters
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # checking for invalid inputs


        # creating the user
        username = username
        password = pass1
        emailID = ''
        user = User.objects.create_user(username,emailID, pass1)
        user.save()

        # try to put a success message here
    else:
        return HttpResponse('404 - found')