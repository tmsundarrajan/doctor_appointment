from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    specialization=models.CharField(max_length=100)
    
def __str__(self):
    return self.user.username

class Patient(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=15)
    
def __str__(self):
    return self.user.username

class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    symptoms=models.TextField()
    status=models.CharField(max_length=20, default='pending')
    
def __str__(self):
    return f"{self.patient} with {self.doctor} on {self.date}"
    

