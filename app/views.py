from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from accounts.views import ProfileUpdateView
from .models import Appointment, Student, Tutor, Review
from django.urls import reverse_lazy
from django.db.models import Sum

from .models import Appointment, Student, Tutor, Review
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'

class AppointmentListView(ListView):
    model = Appointment
    context_object_name = 'appointments'
    template_name = 'app/appointment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q', '')
        if query:
            filtered_appointments = Appointment.objects.filter(appointment__icontains=query).order_by('-pub_date')
        else:
            filtered_appointments = Appointment.objects.all().order_by('-pub_date')
        context['appointments'] = filtered_appointments
        context ['total_appointments'] = Appointment.objects.count()
        context ['total_students'] = Student.objects.count()
        context['total_tutors'] = Tutor.objects.count()
        context['total_reviews'] = Review.objects.count()
        context['total_users'] = get_user_model().objects.all()
        context['sum_appointment_price'] = filtered_appointments.aggregate(Sum('price'))['price__sum'] or 0
        return context


class AppointmentDetailView(DetailView):
    model = Appointment
    context_object_name = 'appointment'
    template_name = 'app/appointment_detail.html'

class AppointmentCreateView(CreateView):
    model = Appointment
    fields = ['appointment', 'user', 'subject', 'student', 'price', 'rating', 'pub_date', 'tutor']
    template_name = 'app/appointment_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = get_user_model().objects.all()
        context['students'] = Student.objects.all()
        context['tutors'] = Tutor.objects.all()
        return context

class AppointmentUpdateView(UpdateView):
    model = Appointment
    fields = ['appointment', 'user', 'subject', 'student', 'price', 'rating', 'pub_date', 'tutor']
    template_name = 'app/appointment_update.html'

class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'app/appointment_delete.html'
    success_url = reverse_lazy('appointment')

class ProfileUpdate(UpdateView):
    model = get_user_model()
    fields = ['username', 'email', 'profile_picture']
    template_name = 'app/profile_update.html'
    success_url = reverse_lazy('Profile')

