from django.contrib import admin
from .models import Appointment, Tutor, Student, Review

admin.site.register(Appointment)
admin.site.register(Tutor)
admin.site.register(Student)
admin.site.register(Review)
