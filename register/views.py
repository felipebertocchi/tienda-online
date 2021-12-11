from django.http import response
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save() #save user in our database
        # once registered we want to redirect the user
        return redirect('/')
    else:
        form = RegisterForm()
        
    context = {"form" : form}
    return render(request, 'register.html', context)
