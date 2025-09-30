"""
Views for the patient app.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from .models import Patient
from .forms import PatientForm, PatientSearchForm

def patient_search(request):
    """View for searching patients by phone number."""
    form = PatientSearchForm(request.GET or None)
    patient = None
    
    if form.is_valid():
        phone = form.cleaned_data['phone']
        try:
            patient = Patient.objects.get(phone=phone)
            return redirect('app_patient:patient_detail', pk=patient.pk)
        except Patient.DoesNotExist:
            messages.error(request, _('No patient found with this phone number.'))
    
    context = {
        'title': _('Patient Search'),
        'form': form,
    }
    return render(request, 'app_patient/patient_search.html', context)

def patient_detail(request, pk):
    """View for displaying patient details."""
    patient = get_object_or_404(Patient, pk=pk)
    appointments = patient.appointment_set.all().order_by('-appointment_date')
    
    context = {
        'title': _('Patient Details'),
        'patient': patient,
        'appointments': appointments,
    }
    return render(request, 'app_patient/patient_detail.html', context)

@login_required
def patient_list(request):
    """View for listing all patients."""
    patients = Patient.objects.all()
    
    context = {
        'title': _('Patient List'),
        'patients': patients,
    }
    return render(request, 'app_patient/patient_list.html', context)

@login_required
def patient_create(request):
    """View for creating a new patient."""
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            messages.success(request, _('Patient created successfully.'))
            return redirect('app_patient:patient_detail', pk=patient.pk)
    else:
        form = PatientForm()
    
    context = {
        'title': _('Create Patient'),
        'form': form,
    }
    return render(request, 'app_patient/patient_form.html', context)

@login_required
def patient_update(request, pk):
    """View for updating a patient."""
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, _('Patient updated successfully.'))
            return redirect('app_patient:patient_detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    
    context = {
        'title': _('Update Patient'),
        'form': form,
        'patient': patient,
    }
    return render(request, 'app_patient/patient_form.html', context)

@login_required
def patient_delete(request, pk):
    """View for deleting a patient."""
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        patient.delete()
        messages.success(request, _('Patient deleted successfully.'))
        return redirect('app_patient:patient_list')
    
    context = {
        'title': _('Delete Patient'),
        'patient': patient,
    }
    return render(request, 'app_patient/patient_confirm_delete.html', context)