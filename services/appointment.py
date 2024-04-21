from fastapi import HTTPException

from schema.doctors import Doctor, doctors
from schema.appointement import Appointment, MakeAppointment, appointments

from logger import logger


class AppointmentService:

    @staticmethod
    def check_doctor_availablity(payload: MakeAppointment):
        doctor_id = payload.doctor_id
        doctor = doctors.get(int(doctor_id))
        if doctor is None:
            raise HTTPException(
                status_code=404, detail="Doctor not found")
        for appointment in appointments:
            if appointment.doctor_id == doctor_id and doctor.is_available is False:
                raise HTTPException(
                    status_code=400, detail="Doctor is not available")

        if doctor.is_available is True:
            doctor.is_available = False
        else:
            logger.warning("Doctor is unavailable")
            raise HTTPException(
                status_code=400, detail="Doctor is unavailable")        

        return payload

    # @staticmethod
    # def check_if_patient(appo)

    @staticmethod
    def appointment_compiler(appointments: list[Appointment]):
        appointment_list = []
        for appointment in appointments:
            appointment_list.append(appointment)
        return appointment_list


appointment_service = AppointmentService()
