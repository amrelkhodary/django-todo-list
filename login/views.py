from django.shortcuts import render
from django import forms
from .models import Users
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

#auth form class
class AuthForm(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=128)

#view to display login page
def auth(request):
    if request.method == "POST":
        #write code to check if data already exists
        #if exists, redirect to app
        #if not, create a new user, redirect to app

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Users(username = username, password = password)

        #add user's username and password to current session
        request.session["user"] = {"username": username, "password": password}

        if not (Users.objects.filter(username = username, password = password).exists()):
           #create a new user 
          user.save()
        
        #redirect to app
        return HttpResponseRedirect(reverse("app:index"))
    
    if request.method == "GET":
        context = {"auth_form": AuthForm()}
        return render(request, 'auth.html', context)
    
