from django.urls import path
from doctors.views import DoctorListCreateView, DoctorDetailView

urlpatterns = [
    # doctors-related endpoints
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

]