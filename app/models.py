from django.db import models
from django.urls import reverse
from django.conf import settings

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Tutor(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

class Appointment(models.Model):
    appointment = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.TextField()
    rating = models.FloatField()
    pub_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    student = models.ManyToManyField(Student)
    tutor = models.ForeignKey("Tutor", on_delete=models.CASCADE)

    def __str__(self):
        return self.appointment

    def get_absolute_url(self):
        return reverse("appointment_detail", kwargs={"pk": self.pk})

class Review(models.Model):
    feedback = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
