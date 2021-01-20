from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'index.html',context)
    #return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')

    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')

    #return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('mob')
        desc = request.POST.get('query')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')

    #return HttpResponse("This is contact page")

