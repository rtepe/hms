from django.urls import path, include

urlpatterns = [
    path('patients/', include('patient_admission.urls')),
    path('inpatients/', include('inpatient.urls')),    
]
