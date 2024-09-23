from django.shortcuts import render
from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework import filters


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'specialty', 'availability']
