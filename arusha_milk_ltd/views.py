from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def menu(request):
    products = Product.objects.all()
    return render(request, 'menu.html', {'products': products})

def reservation(request):
    return render(request, 'reservation.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, email, subject, message)

    return render(request, 'contact.html')

