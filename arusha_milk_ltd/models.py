from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product_name

class CustomerMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class CustomerOrder(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    PRODUCT_CHOICES = [
        ('Fresh Milk 1L', 'Fresh Milk 1L'),
        ('Fresh Milk 1.5L', 'Fresh Milk 1.5L'),
        ('Fresh Milk 5L', 'Fresh Milk 5L'),
        ('Yogurt 1L','Yogurt 1L'),
        ('Yogurt 1.5L', 'Yogurt 1.5L'),
        ('Yogurt5L', 'Yogurt5L'),
    ]

    product = models.CharField(
        max_length=50,
        choices=PRODUCT_CHOICES
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.product}"

class RequestDelivery(models.Model):

    PRODUCT_CHOICES = [
        ('Fresh Milk 1L', 'Fresh Milk 1L'),
        ('Fresh Milk 1.5L', 'Fresh Milk 1.5L'),
        ('Fresh Milk 5L', 'Fresh Milk 5L'),
        ('Yogurt 1L','Yogurt 1L'),
        ('Yogurt 1.5L', 'Yogurt 1.5L'),
        ('Yogurt5L', 'Yogurt5L'),
    ]

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)

    product = models.CharField(max_length=50, choices=PRODUCT_CHOICES)

    delivery_date = models.DateField()
    delivery_time = models.CharField(max_length=100)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.product}"

    class Meta:
        ordering = ['-created_at']
