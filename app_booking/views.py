"""
Views for the booking app.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import PublicBookingForm, AppointmentForm
from app_patient.models import Patient

def public_booking(request):
    """View for public appointment booking."""
    if request.method == 'POST':
        form = PublicBookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            doctor = form.cleaned_data['doctor']
            appointment_date = form.cleaned_data['appointment_date']
            note = form.cleaned_data['note']
            
            # Get or create patient
            patient, created = Patient.objects.get_or_create(
                phone=phone,
                defaults={'name': name}
            )
            
            # Create appointment
            appointment = Appointment.objects.create(
                patient=patient,
                doctor=doctor,
                appointment_date=appointment_date,
                note=note
            )
            
            messages.success(request, _('Appointment booked successfully.'))
            return redirect('app_booking:booking_success', pk=appointment.pk)
    else:
        form = PublicBookingForm()
    
    context = {
        'title': _('Book an Appointment'),
        'form': form,
    }
    return render(request, 'app_booking/public_booking.html', context)

def booking_success(request, pk):
    """View for successful booking."""
    appointment = get_object_or_404(Appointment, pk=pk)
    
    context = {
        'title': _('Booking Successful'),
        'appointment': appointment,
    }
    return render(request, 'app_booking/booking_success.html', context)

@login_required
def appointment_list(request):
    """View for listing all appointments."""
    appointments = Appointment.objects.all()
    
    context = {
        'title': _('Appointment List'),
        'appointments': appointments,
    }
    return render(request, 'app_booking/appointment_list.html', context)

@login_required
def appointment_detail(request, pk):
    """View for displaying appointment details."""
    appointment = get_object_or_404(Appointment, pk=pk)
    
    context = {
        'title': _('Appointment Details'),
        'appointment': appointment,
    }
    return render(request, 'app_booking/appointment_detail.html', context)

@login_required
def appointment_create(request):
    """View for creating a new appointment."""
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            messages.success(request, _('Appointment created successfully.'))
            return redirect('app_booking:appointment_detail', pk=appointment.pk)
    else:
        form = AppointmentForm()
    
    context = {
        'title': _('Create Appointment'),
        'form': form,
    }
    return render(request, 'app_booking/appointment_form.html', context)

@login_required
def appointment_update(request, pk):
    """View for updating an appointment."""
    appointment = get_object_or_404(Appointment, pk=pk)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, _('Appointment updated successfully.'))
            return redirect('app_booking:appointment_detail', pk=appointment.pk)
    else:
        form = AppointmentForm(instance=appointment)
    
    context = {
        'title': _('Update Appointment'),
        'form': form,
        'appointment': appointment,
    }
    return render(request, 'app_booking/appointment_form.html', context)

@login_required
def appointment_delete(request, pk):
    """View for deleting an appointment."""
    appointment = get_object_or_404(Appointment, pk=pk)
    
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, _('Appointment deleted successfully.'))
        return redirect('app_booking:appointment_list')
    
    context = {
        'title': _('Delete Appointment'),
        'appointment': appointment,
    }
    return render(request, 'app_booking/appointment_confirm_delete.html', context)