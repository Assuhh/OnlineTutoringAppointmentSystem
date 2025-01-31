from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (HomePageView, AboutPageView, AppointmentListView,
                    AppointmentDetailView, AppointmentCreateView, AppointmentUpdateView,
                    AppointmentDeleteView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('appointment/', AppointmentListView.as_view(), name='appointment'),
    path('appointment/<int:pk>', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointment/create', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointment/<int:pk>/edit', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointment/<int:pk>/delete', AppointmentDeleteView.as_view(), name='appointment_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)