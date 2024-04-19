from pydantic import BaseModel


class Patient(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: float
    height: float
    phone: str


class PatientCreate(BaseModel):
    name: str
    age: int
    sex: str
    weight: int
    height: float
    phone: str


patients = {
    1: Patient(id=1, name="John Doe", age=30, sex="Male", weight=65, height=50, phone="08092458875"),
    2: Patient(id=2, name="Ayo Deji", age=62, sex="Male", weight=75, height=40, phone="08130458835"),
    3: Patient(id=3, name="Ade Kemi", age=24, sex="Female", weight=55, height=30, phone="09092454530"),
}
