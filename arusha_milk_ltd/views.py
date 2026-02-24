from django.shortcuts import render, redirect
from .forms import RequestDeliveryForm
from django.contrib import messages
from .models import Product, CustomerMessage, CustomerOrder

def index(request):

    products = Product.objects.all()

    if request.method == "POST":

        CustomerOrder.objects.create(

            name=request.POST.get('name'),

            email=request.POST.get('email'),

            phone=request.POST.get('phone'),

            product=request.POST.get('product')

        )

        messages.success(request,"Order Sent Successfully!")

        return redirect('https://greenlandcompanyltd.pythonanywhere.com/arusha_milk_ltd/')


    return render(request,'index.html',{
        'products':products
    })

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def menu(request):
    products = Product.objects.all()
    return render(request, 'menu.html', {'products': products})

def reservation(request):
    success = False

    if request.method == "POST":
        form = RequestDeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://greenlandcompanyltd.pythonanywhere.com/arusha_milk_ltd/reservation/')  # prevents resubmission on refresh
    else:
        form = RequestDeliveryForm()

    return render(request, 'reservation.html', {
        'form': form,
        'success': success
    })

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        CustomerMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('https://greenlandcompanyltd.pythonanywhere.com/arusha_milk_ltd/contact/')

    return render(request, 'infor.html')
