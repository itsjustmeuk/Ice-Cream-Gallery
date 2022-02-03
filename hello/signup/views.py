from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
import re

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']

        #Sanitizing inputs
        if len(username) > 15 or len(username) < 8:
            messages.warning(request, "Username length must be between 8 to 15 characters.")
            return redirect("/register")
        
        if not username.isalnum():
            messages.warning(request, "Username must be alphanumeric.")
            return redirect("/register")

        if User.objects.filter(username=username):
            messages.warning(request, "Username already exists.")
            return redirect("/register")
        
        if User.objects.filter(email=email):
            messages.warning(request, "Email already registered.")
            return redirect("/register")
        
        if pass1 != pass2:
            messages.warning(request, "Passwords don't match.")
            return redirect("/register")

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(regex, email)):
            messages.error(request, "Enter correct email.")
            return redirect("/register")
        

        #Create User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.fname = fname
        myuser.lname = lname
        myuser.save()

        #Success Message
        messages.success(request, "Your account has been successfully created.")
        return render(request, "login.html")
    else: 
        return render(request, "register.html")