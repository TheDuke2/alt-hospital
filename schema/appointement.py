from pydantic import BaseModel
from typing import Union
from schema.doctors import Doctor


class Appointment(BaseModel):
    id: int
    patient_id: int
    doctor_id: Union[int, Doctor] 
    date: str 
    is_complete: bool = False


class MakeAppointment(BaseModel):
    patient_id: int
    doctor_id:  Union[int, Doctor] 
    date: str


appointments = [
    Appointment(id=1, patient_id=1, doctor_id=2, date='2024-04-12')
]
