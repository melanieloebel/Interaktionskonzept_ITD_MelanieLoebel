import paho.mqtt.client as mqtt
import json
import time
import datetime
import appointment


class Doctor():

    #Konstruktor
    def __init__(self, title, name, specialist, phoneno):
        self.title = title
        self.name = name
        self.specialist = specialist
        self.phoneno = phoneno
      

doctors = []


def save_appointment(self, patient_name, app_date):
        self.patient_name = patient_name
        self.app_date = app_date

        #Input name of patient
        patient_name = input("Please enter your name: ")

        #Input and parse of wish appointment
        request_date = datetime.strptime(input ("Please enter your wish appointment in format YYYY-MM-DD: "), "%Y-%m-%d")

        #Format appointment
        app_date = request_date.strftime("%d.%m.%Y")
        
        print (app_date)
       
        


        
doc1 = Doctor('Dr.','Mel','Innere Medizin','123')
doc1.save_appointment




#Event, dass beim Verbindungsaufbau aufgerufen wird
#def on_connect(client, userdata, flags, rc):
#    client.subscribe([                    
#                    ("hshl/hospitals/hospital_1", 2),
#                    ])
# muss dieses Event so aufgerufen werden ???

#doctor_1 = Doctor("Dr.", "Klaus Topp", "Innere Medizin", "02941-111111")
#print (doctor_1.name)
