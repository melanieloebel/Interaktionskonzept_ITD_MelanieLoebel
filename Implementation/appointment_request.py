import paho.mqtt.client as mqtt
import json
import time

ask = True

def on_connect(client, userdata, flags, rc):
    client.subscribe([
                    ("hshl/???", 2), #topic is missing, maybe "hshl/hospitals/hospital_1/appointment_request"
                    ])

def on_message(client, userdata, msg):
    global ask 
    ask = True
    print(str(msg.payload))
    

client = mqtt.Client()
client.on_connect = on_connect #Zuweisen des Connect Events
client.on_message = on_message #Zuweisen des Message Events

client.username_pw_set("solace-cloud-client", "nbsse0pkvpkvhpeh3ll5j7rpha") # Benutzernamen und Passwort zur Verbindung setzen

client.connect("mr2mbqbl71a4vf.messaging.solace.cloud", port = 20614) #Verbindung zum Broker aufbauen

client.loop_start()


def appointment_request (patient_name, date_request): #, specialist):
     data = {
        "patient name": patient_name,
        "date request": date_request,
        #"specialist": specialist,
        "topic": "hshl/???",    #topic is missing
    }
    client.publish("hshl/???", json.dumps(data))

while True:
    if ask:
        patient_name = input("Please enter your name: ")
        date_request = input("Please enter your appointment request with format DD.MM.YYYY: ")
        #specialist = input("Please enter the specialist :") #hier implementieren?
        appointment_request(patient_name, date_request)
        ask = False
