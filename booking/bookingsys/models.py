from django.db import models
from django.contrib.auth.models import User  # Import User model
from django.core.exceptions import ValidationError
from datetime import timedelta

class Booking(models.Model):
    ROOM_CHOICES = [
        ('Room 1', 'Room 1'),
        ('Room 2', 'Room 2'),
        ('Room 3', 'Room 3'),
    ]
    room = models.CharField(max_length=20, choices=ROOM_CHOICES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # ForeignKey to User model

    def clean(self):
        # Ensure the end time is after the start time
        if self.end_time <= self.start_time:
            raise ValidationError("End time must be after the start time.")

        # Check if the room is already booked
        conflicting_bookings = Booking.objects.filter(
            room=self.room,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        )
        if conflicting_bookings.exists():
            raise ValidationError("This room is already booked during the selected time range.")
        
    def __str__(self):
        return f"Booking for {self.room} from {self.start_time} to {self.end_time}"
