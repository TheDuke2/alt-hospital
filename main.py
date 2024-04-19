from fastapi import FastAPI

from routers.patients import patient_router
from routers.doctors import doctor_router
from routers.appointments import appointment_router

app = FastAPI()

app.include_router(patient_router, prefix='/patient', tags=['patient'])
app.include_router(doctor_router, prefix='/doctor', tags=['doctor'])
app.include_router(appointment_router, prefix='/appointment', tags=['appointment'])

@app.get('/')
def home():
    return {"message": "Welcome Let's Create Magic"}
