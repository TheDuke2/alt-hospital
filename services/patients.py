# from fastapi import HTTPException

# from schema.patients import PatientCreate, Patient, patients


# class PatientService:
    
#     @staticmethod
#     def get_current_patient(patient_id: int, payload: PatientCreate):
#         curr_patient = patients[patient_id]
#         patient_id = payload.
#         if curr_patient is None:
#             raise HTTPException(status_code=404, detail="Patient not found")
#         return curr_patient
