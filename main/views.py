from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Blog, CustomerMessage, TeamMember


def main(request):
    blogs = Blog.objects.all()
    team_members = TeamMember.objects.all()

    context = {
        'blogs': blogs,
        'team_members': team_members
    }

    return render(request, 'main.html', context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        CustomerMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        # # Email to Company
        # send_mail(
        #     subject=f"New Message from {name}",
        #     message=f"""
        #     Name: {name}
        #     Email: {email}
        #     Phone: {phone}

        #     Message:
        #     {message}
        #     """,
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=['greenlandltd@gmail.com'],
        # )

        # # Auto Reply to Customer
        # send_mail(
        #     subject="Thank you for contacting Green Land Company Ltd",
        #     message=f"""
        #     Dear {name},

        #     Thank you for contacting Green Land Company Ltd.
        #     We have received your message and our team will respond shortly.

        #     Best Regards,
        #     Green Land Company Ltd
        #     Dar es Salaam, Tanzania
        #     """,
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[email],
        # )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contacts')

    return render(request, 'contact.html')