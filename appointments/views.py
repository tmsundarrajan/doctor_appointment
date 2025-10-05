from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Doctor, Patient, Appointment


def home(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    if hasattr(request.user, 'patient'):
        appointments=Appointment.objects.filter(patient=request.user.patient)
    elif hasattr(request.user, 'doctor'):
        appointments=Appointment.objects.filter(doctor=request.user.doctor)
    else:
        appointments=[]
    return render(request, 'dashboard.html', {'appointments':appointments})

@login_required
def book_appointment(request):
    if request.method=="POST":
        doctor_id=request.POST['doctor']
        date=request.POST['date']
        time=request.POST['time']
        symptoms=request.POST['symptoms']
        
        doctor=Doctor.objects.get(id=doctor_id)
        patient=request.user.patient
        
        Appointment.objects.create(doctor=doctor, patient=patient, date=date, time=time, symptoms=symptoms)
        return redirect('dashboard')
    
    doctors=Doctor.objects.all()
    return render(request, 'book_appointment.html', {'doctors':doctors})


