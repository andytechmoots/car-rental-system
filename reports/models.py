from django.db import models
from rentals.models import Rental

class Report(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    issue = models.TextField()
    reported_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for Rental ID {self.rental.id}"
