from mongoengine import Document, StringField, DateField

class Book(Document):
    title = StringField(max_length=100, required=True)
    author = StringField(max_length=50, required=True)
    published_date = DateField()
