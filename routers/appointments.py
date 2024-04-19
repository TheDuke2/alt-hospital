from fastapi import APIRouter, HTTPException, Depends

from schema.appointement import Appointment, MakeAppointment, appointments
from schema.patients import Patient, patients
from services.appointment import appointment_service

appointment_router = APIRouter()

# Create a new appointment


@appointment_router.post('/{patient_id}', status_code=200)
def create_appointment(patient_id: int, payload: MakeAppointment = Depends(appointment_service.check_doctor_availablity)):
    # patient_id: int = payload.patient_id
    curr_patient = patient_id
    if curr_patient in patients:
        patient: Patient = patients.get(int(curr_patient))
        if patient.id != patient_id:
            raise HTTPException(
                status_code=400,
                detail=f'Patient with id {patient_id} does not exist'
            )
    doctor_id: int = payload.doctor_id

    # create appointment ID
    appointment_id = len(appointments) + 1
    # make appointment
    new_appointment = Appointment(
        id=appointment_id,
        patient_id=patient_id,
        doctor_id=doctor_id,
        date=payload.date
        is_pending= True,
    )
    appointments.append(new_appointment)
    return {'message': 'Appointment created successfully', 'data': new_appointment}

# Retrieve Appointments


@appointment_router.get('/', status_code=200)
def appointment_list():
    appointment_list = appointment_service.appointment_compiler(appointments)
    return {'message': 'success', 'data': appointment_list}

# # Complete appointment
# @appointment_router.post('/{patient_id}', status_code=200)
# def appointment_complete():