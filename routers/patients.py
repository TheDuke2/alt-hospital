from fastapi import APIRouter, HTTPException
from schema.patients import Patient, PatientCreate, patients

patient_router = APIRouter()

# Create a new Patient
# @patient_router.post('/', status_code=201)
# def create_patient(payload: PatientCreate):
#     patient_id  = len(patients) + 1
#     for new_patient in patients:
#         if new_patient.name == payload.name:
#             raise HTTPException(status_code=400, detail="Patient already exists")
#     new_patient = Patient(
# id = patient_id,
# name = payload.name,
# age = payload.age,
# sex = payload.sex,
# weight = payload.weight,
# height = payload.height,
# phone = payload.phone,
#         )
#     patients.append(new_patient)
#     return {'message': 'New patient created sucessfully', 'data': new_patient}


@patient_router.post('/', status_code=201)
def create_product(payload: PatientCreate):
    # get the product id
    patient_id = len(patients) + 1
    new_patient = Patient(
        id=patient_id,
        name=payload.name,
        age=payload.age,
        sex=payload.sex,
        weight=payload.weight,
        height=payload.height,
        phone=payload.phone,
    )
    patients[patient_id] = new_patient
    return {'message': 'New patient created successfully', 'data': new_patient}

# Retrieve all Patients


@patient_router.get('/', status_code=200)
def patient_list():
    return {'message': 'success', 'data': patients}

# Update patient


@patient_router.put('/{patient_id}', status_code=200)
def patient_update(patient_id: int, payload: PatientCreate):
    current_patient = patients[patient_id]

    if current_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    current_patient.name = payload.name
    current_patient.age = payload.age
    current_patient.sex = payload.sex
    current_patient.weight = payload.weight
    current_patient.height = payload.height
    current_patient.phone = payload.phone
    return {'message': 'Patient updated successfully', 'data': current_patient}

# Delete patient


@patient_router.delete('/{patient_id}', status_code=200)
def patient_delete(patient_id: int):
    patient = patients[patient_id]

    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    del patients[patient]
    return {'message': 'Patient deleted successfully', 'data': patient}
