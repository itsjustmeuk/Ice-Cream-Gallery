from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

# Create your views here.
def loginUser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/")
        # Redirect to a success page.
    else:
        # Return an 'invalid login' error message.
        return render(request, "login.html")