from fastapi import APIRouter, HTTPException

from schema.doctors import Doctor, DoctorCreate, doctors


doctor_router = APIRouter()


@doctor_router.post('/', status_code=201)
def create_doctor(payload: DoctorCreate):
    doctor_id = len(doctors)

    new_doctor = Doctor(
        id=doctor_id,
        name=payload.name,
        specialization=payload.specialization,
        phone_number=payload.phone_number
    )

    doctors[doctor_id] = new_doctor
    return {'message': "New doctor created successfully",  'data': new_doctor}


@doctor_router.get('/{doctor_id}', status_code=200)
def get_doctor_by_id(doctor_id: int):
    doctor = doctors.get(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {'message': "success", 'data': doctor}


@doctor_router.get('/', status_code=200)
def doctor_list():
    return {'message': "success", 'data': doctors}


@doctor_router.put('/{doctor_id}', status_code=201)
def edit_doctor(doctor_id: int, payload: DoctorCreate):
    current_doctor = doctors.get(int(doctor_id))

    if current_doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    current_doctor.name = payload.name
    current_doctor.specialization = payload.specialization
    current_doctor.phone_number = payload.phone_number
    return {'message': "New doctor created successfully",  'data': current_doctor}


@doctor_router.delete('/{doctor_id}', status_code=204)
def delete_doctor(doctor_id: int):
    doctor = doctors[doctor_id]

    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    del doctors[doctor_id]
    return {'message': 'Doctor deleted successfully'}


@doctor_router.patch('/{doctor_id}', status_code=200)
def set_available_status(doctor_id: int):
    # Check if doctor_id exists in the dictionary
    if doctor_id not in doctors:
        raise HTTPException(status_code=404, detail="Doctor not found")

    # Update the availability status of the doctor
    doctor = doctors[doctor_id]
    doctor.is_available = False

    # Return response with updated doctor information
    return {'message': "Availability status changed successfully", 'data': doctor}
