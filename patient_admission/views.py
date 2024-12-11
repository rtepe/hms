from django.shortcuts import render, redirect
from .models import Patient
from datetime import datetime

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_admission/patient_list.html', {'patients': patients})

def patient_register(request):
    if request.method == 'POST':
        Patient(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            dob=request.POST.get('dob'),
            contact_number=request.POST.get('contact_number'),
            address=request.POST.get('address'),
            admission_date=datetime.now()
        ).save()
        return redirect('patient_list')
    return render(request, 'patient_admission/patient_register.html')
