from django.db import models

# Create your models here.
class reader(models.Model):
    def __str__(self):
        return self.reader_name
    reference_id=models.CharField(max_length=200)
    reader_name=models.CharField(max_length=200)
    reader_contact=models.CharField(max_length=200)
    reader_address=models.TextField()
    active=models.BooleanField(default=True)

class books(models.Model):
    def __str__(self):
        return self.books_name
    reference_id=models.CharField(max_length=200)
    book_name=models.CharField(max_length=200)
    authors=models.CharField(max_length=200)
    book_id=models.TextField()
    description=models.BooleanField(default=True)
