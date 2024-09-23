from django.urls import path
from appointments.views import AppointmentListCreateView, AppointmentDetailView

urlpatterns = [
    # User-related endpoints
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),

]