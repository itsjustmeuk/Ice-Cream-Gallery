from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from myapp.models import Contact

# Create your views here.
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today()) 
        contact.save()
        messages.success(request, 'Your Message has been sent!')

    return render(request, "error.html")