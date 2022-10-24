#FastAPI
from fastapi import FastAPI

#Archivos src
from src.controller import send_verify_number_phone, validate_verification_code
from src.schema import mobile_numbers, verification_code

app = FastAPI()

#API para solicitar el numero de celular y enviar SMS

@app.post("/sms", name="SMS")
def send_message(mobile_numbers: mobile_numbers):
    number = mobile_numbers.mobileNumbers
    response = send_verify_number_phone(number)
    return response

#API para verificar codigo generado

@app.post("/verification_code", name="VERIFICATION_CODE")
def validate_code(verification_code: verification_code):
    response = validate_verification_code(verification_code)
    return response