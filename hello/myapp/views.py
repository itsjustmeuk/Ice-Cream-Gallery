from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login/")
    else:
        return render(request, "index.html")

def about(request):
    if request.user.is_anonymous:
        return redirect("/login/")
    else:
        return render(request, "about.html")

def services(request):
    if request.user.is_anonymous:
        return redirect("/login/")
    else:
        return render(request, "services.html")

def error(request):
    return render(request, "404.html")