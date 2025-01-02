from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm, LoginForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from datetime import datetime
from datetime import timedelta
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required  # Import the login_required decorator

# Booking View
@login_required  # Ensure that the user is logged in before they can access this view
def booking(request):
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

# Booking Success View
def booking_success(request):
    return render(request, 'booking_success.html')

# Sign Up View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')  # Redirect to login after successful sign-up
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

# Custom Login View
def custom_login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('booking')  # Redirect to booking page after successful login
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)  # Logs the user out
    messages.success(request, "You have been logged out.")  # Optional success message
    return render(request, 'logout.html')  # Render the logout page instead of redirecting