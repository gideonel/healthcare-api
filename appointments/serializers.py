from rest_framework import serializers
from .models import Appointment
from users.serializers import UserSerializer
from doctors.serializers import DoctorSerializer

class AppointmentSerializer(serializers.ModelSerializer):
    patient = UserSerializer()  # Nest UserSerializer for patient
    doctor = DoctorSerializer()  # Nest DoctorSerializer for doctor

    class Meta:
        model = Appointment
        fields = ('id', 'date', 'time', 'status', 'patient', 'doctor')

