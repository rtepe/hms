from mongoengine import Document, StringField, DateField

class Patient(Document):
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)
    dob = DateField(required=True)
    contact_number = StringField(max_length=15, required=True)
    address = StringField()
    admission_date = DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
