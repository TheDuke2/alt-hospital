from fastapi import HTTPException

from schema.patients import PatientCreate, Patient, patients

from logger import logger


class PatientService:
    @staticmethod
    def check_current_patient(patient_id: int):
        if patient_id in patients:
            current_patient: Patient = patients.get(int(patient_id))
            if current_patient.id != patient_id:
                logger.warning("Patient doesn't exist")
                raise HTTPException(
                    status_code=400,
                    detail=f'Patient with id {patient_id} does not exist'
                )
        return patient_id


patient_service = PatientService()
