from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Your account has been registered successfully")
            return redirect('login')
    else:
        form = UserCreationForm
    
    form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})