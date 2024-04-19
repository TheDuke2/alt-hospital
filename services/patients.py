from fastapi import HTTPException

from schema.patients import PatientCreate, Patient, patients

from logger import logger


class PatientService:
    @staticmethod
    def get_current_patient(patient_id: int):
        if patient_id in patients:
            patient: Patient = patients.get(int(patient_id))
            if patient.id != patient_id:
                logger.warning("Patient doesn't exist")
                raise HTTPException(
                    status_code=400,
                    detail=f'Patient with id {patient_id} does not exist'
                )
        return patient_id


patient_service = PatientService()
#         curr_patient = patients[patient_id]
#         patient_id = payload.
#         if curr_patient is None:
#             raise HTTPException(status_code=404, detail="Patient not found")
#         return curr_patient
