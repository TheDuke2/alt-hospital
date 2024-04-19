from fastapi import APIRouter, HTTPException, Depends

from schema.appointement import Appointment, MakeAppointment, appointments
from schema.patients import Patient, patients
from services.appointment import appointment_service
from services.patients import patient_service

appointment_router = APIRouter()

# Create a new appointment


@appointment_router.post('/{patient_id}', status_code=200)
def create_appointment(payload: MakeAppointment = Depends(appointment_service.check_doctor_availablity), curr_patient: Patient = Depends(patient_service.get_current_patient)):
    doctor_id: int = payload.doctor_id

    if curr_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")

    if doctor_id is None:
        raise HTTPException(status_code=404, detail="Doctor not found")

    # create appointment ID
    appointment_id = len(appointments) + 1
    # make appointment
    new_appointment = Appointment(
        id=appointment_id,
        patient_id=curr_patient,
        doctor_id=doctor_id,
        date=payload.date,
    )
    appointments.append(new_appointment)
    return {'message': 'Appointment created successfully', 'data': new_appointment}

# Retrieve Appointments


@appointment_router.get('/', status_code=200)
def appointment_list():
    appointment_list = appointment_service.appointment_compiler(appointments)
    return {'message': 'success', 'data': appointment_list}

# Complete appointment
# @appointment_router.post('/{patient_id}', status_code=200)
# def appointment_complete(patient_id: int, payload: MakeAppointment = Depends(appointment_service.check_doctor_availablity)):
