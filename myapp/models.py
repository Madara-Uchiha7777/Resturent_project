from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
