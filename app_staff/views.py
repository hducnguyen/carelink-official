"""
Views for the staff app.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from .models import Staff
from .forms import StaffForm, StaffUserCreationForm
from app_booking.models import Appointment

def is_admin(user):
    """Check if the user is an admin."""
    try:
        return user.is_authenticated and user.staff_profile.role == 'admin'
    except:
        return False

@login_required
def dashboard(request):
    """View for the staff dashboard."""
    # Get today's appointments
    today_appointments = Appointment.objects.filter(
        doctor__user=request.user,
        status__in=['scheduled', 'confirmed']
    ).order_by('appointment_date')
    
    context = {
        'title': _('Staff Dashboard'),
        'today_appointments': today_appointments,
    }
    return render(request, 'app_staff/dashboard.html', context)

@login_required
@user_passes_test(is_admin)
def staff_list(request):
    """View for listing all staff members."""
    staff_members = Staff.objects.all()
    
    context = {
        'title': _('Staff List'),
        'staff_members': staff_members,
    }
    return render(request, 'app_staff/staff_list.html', context)

@login_required
def staff_detail(request, pk):
    """View for displaying staff details."""
    staff = get_object_or_404(Staff, pk=pk)
    
    context = {
        'title': _('Staff Details'),
        'staff': staff,
    }
    return render(request, 'app_staff/staff_detail.html', context)

@login_required
@user_passes_test(is_admin)
def staff_create(request):
    """View for creating a new staff member."""
    if request.method == 'POST':
        user_form = StaffUserCreationForm(request.POST)
        staff_form = StaffForm(request.POST)
        
        if user_form.is_valid() and staff_form.is_valid():
            with transaction.atomic():
                user = user_form.save()
                staff = staff_form.save(commit=False)
                staff.user = user
                staff.save()
                
            messages.success(request, _('Staff member created successfully.'))
            return redirect('app_staff:staff_detail', pk=staff.pk)
    else:
        user_form = StaffUserCreationForm()
        staff_form = StaffForm()
    
    context = {
        'title': _('Create Staff Member'),
        'user_form': user_form,
        'staff_form': staff_form,
    }
    return render(request, 'app_staff/staff_form.html', context)

@login_required
@user_passes_test(is_admin)
def staff_update(request, pk):
    """View for updating a staff member."""
    staff = get_object_or_404(Staff, pk=pk)
    
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, _('Staff member updated successfully.'))
            return redirect('app_staff:staff_detail', pk=staff.pk)
    else:
        form = StaffForm(instance=staff)
    
    context = {
        'title': _('Update Staff Member'),
        'form': form,
        'staff': staff,
    }
    return render(request, 'app_staff/staff_update.html', context)

@login_required
@user_passes_test(is_admin)
def staff_delete(request, pk):
    """View for deleting a staff member."""
    staff = get_object_or_404(Staff, pk=pk)
    
    if request.method == 'POST':
        user = staff.user
        staff.delete()
        user.delete()
        messages.success(request, _('Staff member deleted successfully.'))
        return redirect('app_staff:staff_list')
    
    context = {
        'title': _('Delete Staff Member'),
        'staff': staff,
    }
    return render(request, 'app_staff/staff_confirm_delete.html', context)