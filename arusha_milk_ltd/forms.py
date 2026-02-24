from django import forms
from .models import RequestDelivery

class RequestDeliveryForm(forms.ModelForm):

    delivery_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control bg-transparent border-primary p-4 datetimepicker-input',
            'placeholder': 'Preferred Delivery Date'
        })
    )

    class Meta:
        model = RequestDelivery
        fields = '__all__'

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'placeholder': 'Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'placeholder': 'Email Address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'placeholder': 'Phone (e.g. 0760 144 638)'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'placeholder': 'Delivery Address (street/area)'
            }),
            'product': forms.Select(attrs={
                'class': 'custom-select bg-transparent border-primary px-4',
                'style': 'height:49px;'
            }),
            'delivery_time': forms.TimeInput(attrs={
                'class': 'form-control bg-transparent border-primary p-4 datetimepicker-input',
                'placeholder': 'Preferred Time (e.g. 6–8 AM)',
                'type': 'time'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'rows': 2,
                'placeholder': 'Additional notes (quantity, special instructions)'
            }),
        }


class RequestDeliveryForm(forms.ModelForm):

    delivery_date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control bg-transparent border-primary p-4 datetimepicker-input',
            'placeholder': 'Preferred Delivery Date'
        })
    )

    class Meta:
        model = RequestDelivery
        fields = [
            'full_name',
            'email',
            'phone',
            'address',
            'product',
            'delivery_date',
            'delivery_time',
            'notes'
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'placeholder': 'Full Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'placeholder': 'Email Address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'placeholder': 'Phone (e.g. 0760 144 638)'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'placeholder': 'Delivery Address (street/area)'
            }),
            'product': forms.Select(attrs={
                'class': 'custom-select bg-transparent border-primary px-4',
                'style': 'height:49px;'
            }),
            'delivery_time': forms.TimeInput(attrs={
                'class': 'form-control bg-transparent border-primary p-4 datetimepicker-input',
                'placeholder': 'Preferred Time (e.g. 6–8 AM)',
                'type': 'time'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control bg-transparent border-primary p-4',
                'rows': 2,
                'placeholder': 'Additional notes (quantity, special instructions)'
            }),
        }
