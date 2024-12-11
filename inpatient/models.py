from mongoengine import Document, StringField, ReferenceField, DateField

from patient_admission.models import Patient

class Room(Document):
    room_number = StringField(max_length=10, required=True, unique=True)
    is_occupied = StringField(default=False)  # Store as a string to stay compatible with MongoDB

    def __str__(self):
        return f"Room {self.room_number} - {'Occupied' if self.is_occupied == 'True' else 'Available'}"

class InpatientRecord(Document):
    patient = ReferenceField(Patient, required=True)  # Link to Patient document
    room = ReferenceField(Room, required=True)  # Link to Room document
    admission_date = DateField()
    discharge_date = DateField(null=True)

    def __str__(self):
        return f"Inpatient Record for {self.patient.first_name} {self.patient.last_name}"
