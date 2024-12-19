from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from django.core.exceptions import ValidationError  # Import ValidationError
from datetime import datetime
from datetime import timedelta

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Assign the logged-in user to the booking before saving
            form.instance.user = request.user
            form.save()

            # Success message after form submission
            messages.success(request, "Your booking was successful!")
            return redirect('booking_success')  # Redirect to success page
    else:
        form = BookingForm()

    # Show available rooms for the user based on selected times
    rooms = ['Room 1', 'Room 2', 'Room 3']
    availability = {}
    
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')

    if start_time and end_time:
        start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M')
        end_time = datetime.strptime(end_time, '%Y-%m-%dT%H:%M')

        # Check availability for each room based on selected time
        for room in rooms:
            conflicting_bookings = Booking.objects.filter(
                room=room,
                start_time__lt=end_time,
                end_time__gt=start_time
            )

            availability[room] = "Available" if not conflicting_bookings.exists() else "Booked"

    return render(request, 'booking_form.html', {
        'form': form,
        'availability': availability,
    })

def booking_success(request):
    return render(request, 'booking_success.html')
