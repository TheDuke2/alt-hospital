from pydantic import BaseModel

class Doctor(BaseModel):
    id: int
    name: str
    specialization: str
    phone_number: str
    is_available: bool = True
    
    
class DoctorCreate(BaseModel):
    name: str
    specialization: str
    phone_number: str
    
doctors = {
    0: Doctor(id=0, name="Fat Joe", specialization='orthopedist', phone_number='09045898979'),
    1: Doctor(id=1, name="Ade Tiger", specialization='dermatologist', phone_number='09045898979'),
    2: Doctor(id=2, name="Ayo Ika", specialization='cardiologist', phone_number='09045898979'),
}