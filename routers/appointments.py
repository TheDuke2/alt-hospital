from fastapi import APIRouter, HTTPException, Depends

from schema.appointement import Appointment, MakeAppointment, appointments
from schema.patients import patients
from schema.doctors import doctors
from services.appointment import appointment_service

appointment_router = APIRouter()

# Create a new appointment


@appointment_router.post('/{patient_id}', status_code=200)
def create_appointment(
    patient_id: int,
    payload: MakeAppointment = Depends(
        appointment_service.check_doctor_availablity),
):
    current_patient = patients.get(int(patient_id))
    if current_patient is None:
        raise HTTPException(
            status_code=404, detail=f"Patient with ID {patient_id} does not exist")
    doctor_id: int = payload.doctor_id
    # create appointment ID
    appointment_id = len(appointments)
    # make appointment
    new_appointment = Appointment(
        id=appointment_id,
        patient_id=current_patient.id,
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


@appointment_router.put('/{patient_id}', status_code=200)
def appointment_complete(patient_id: int, appointment_id: int):
    # current_patient = patient_service.check_current_patient(patient_id)
    for appointment in appointments:
        if appointment.patient_id != patient_id and appointment.id == appointment_id:
            raise HTTPException(
                status_code=401, detail="Patient cannot access appointment")

    if appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    appointment.is_complete = True

    doctor_id = appointment.doctor_id
    doctor = doctors.get(int(doctor_id))
    doctor.is_available = True

    return {'message': 'Appointment completed successfully', 'data': appointment}


@appointment_router.delete('/{patient_id}', status_code=200)
def cancel_appointment(appointment_id: int, patient_id: int):
    for appointment in appointments:
        if appointment.id == appointment_id and appointment.patient_id == patient_id:
            appointments.remove(appointment)
            doctor_id = appointment.doctor_id
            doctor = doctors.get(int(doctor_id))

            doctor.is_available = True
            return {'message': 'Appointment cancelled successfully'}
    raise HTTPException(status_code=404, detail="Appointment not found")

    # appointment = None
    # for appointment in appointments:
    #     if appointment.id == appointment_id:
    #         del appointment[appointment_id]
    #         break
    #     else:
    #         raise HTTPException(
    #             status_code=404, detail="Appointment not found")
