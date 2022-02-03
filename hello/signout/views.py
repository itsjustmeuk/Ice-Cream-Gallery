from django.shortcuts import redirect
from django.contrib.auth import logout

# Create your views here.
def logoutUser(request):
    logout(request)
    return redirect("/login/")