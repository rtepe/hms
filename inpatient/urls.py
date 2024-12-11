from django.urls import path
from . import views

urlpatterns = [
    path('', views.inpatient_list, name='inpatient_list'),
    path('admit/', views.admit_patient, name='admit_patient'),
]
