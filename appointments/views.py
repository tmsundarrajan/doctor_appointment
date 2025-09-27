from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor, Patient, Appointment


def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    if hasattr(request.user, 'doctor'):
        appointments=Appointment.objects.filter(doctor=request.user.doctor)
    elif hasattr(request.user, 'patient'):
        appointments=Appointment.objects.filter(patient=request.user.patient)
    else:
        appointments=None
    return render(request, 'dashboard.html', {'appointments':appointments})



