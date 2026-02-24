from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    image = models.ImageField(upload_to='blogs/')

    author = models.CharField(max_length=100)

    date = models.DateField()

    external_link = models.URLField(
        blank=True,
        null=True
    )


    def __str__(self):

        return self.title

class CustomerMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='team/')
    instagram = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name