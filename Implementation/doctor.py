import paho.mqtt.client as mqtt
import json
import time
import datetime
import appointment
from datetime import *
from appointment import *

class Doctor():

    #Konstruktor
    def __init__(self, title, name, specialist, phoneno): #, res_appointments):
        self.title = title
        self.name = name
        self.specialist = specialist
        self.phoneno = phoneno
        #self.res_appointments = res_appointments


doctors = []
#res_appointments = []


def save_appointment(self, patient_name, app_date):
        self.patient_name = input("Please enter your name: ")
        request_date = datetime.strptime(input ("Please enter your wish appointment in format YYYY-MM-DD: "), "%Y-%m-%d")
        
        self.app_date = request.strftime("%d.%m.%Y")
        
        print (app_date)


        #res_appointment.append(patient_name, date, time)

doc1 = Doctor()
doc1.save_appointment()




#Event, dass beim Verbindungsaufbau aufgerufen wird
#def on_connect(client, userdata, flags, rc):
#    client.subscribe([                    
#                    ("hshl/hospitals/hospital_1", 2),
#                    ])
# muss dieses Event so aufgerufen werden ???

#doctor_1 = Doctor("Dr.", "Klaus Topp", "Innere Medizin", "02941-111111")
#print (doctor_1.name)
