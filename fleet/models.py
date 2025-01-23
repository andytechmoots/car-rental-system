from django.db import models

class Vehicle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    license_plate = models.CharField(max_length=20, unique=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('available', 'Available'),
            ('rented', 'Rented'),
            ('maintenance', 'Maintenance'),
        ],
        default='available',
    )

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate})"
