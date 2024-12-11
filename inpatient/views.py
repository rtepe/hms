from django.shortcuts import render, redirect
from .models import Room, InpatientRecord
from patient_admission.models import Patient
from datetime import datetime

def inpatient_list(request):
    records = InpatientRecord.objects.all()
    return render(request, 'inpatient/inpatient_list.html', {'records': records})

def admit_patient(request):
    if request.method == 'POST':
        patient = Patient.objects.get(id=request.POST.get('patient'))
        room = Room.objects.get(id=request.POST.get('room'))
        room.is_occupied = "True"
        room.save()
        InpatientRecord(
            patient=patient,
            room=room,
            admission_date=datetime.now()
        ).save()
        return redirect('inpatient_list')
    patients = Patient.objects.all()
    rooms = Room.objects.filter(is_occupied="False")
    return render(request, 'inpatient/admit_patient.html', {'patients': patients, 'rooms': rooms})
