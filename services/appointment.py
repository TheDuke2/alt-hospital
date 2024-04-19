from fastapi import HTTPException

from schema.doctors import Doctor, doctors
from schema.appointement import Appointment, MakeAppointment

from logger import logger


class AppointmentService:

    @staticmethod
    def check_doctor_availablity(payload: MakeAppointment):
        doctor_id = payload.doctor_id
        if doctor_id in doctors:
            doctor: Doctor = doctors.get(int(doctor_id))
            if doctor.is_available is False:
                logger.warning("Doctor is unavailable")
                raise HTTPException(
                    status_code=400, detail="Doctor is unavailable")
            doctor.is_available = False
        return payload

    @staticmethod
    def appointment_compiler(appointments: list[Appointment]):
        appointment_list = []
        for appointment in appointments:
            appointment_list.append(appointment)
        return appointment_list
        

appointment_service = AppointmentService()
