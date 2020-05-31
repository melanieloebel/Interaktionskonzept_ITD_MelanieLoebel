import paho.mqtt.client as mqtt
import json
from doctor import *

class Hospital:
    def __init__(self, name, adress, phone_no, opening_hours):
        self.name = name
        self.adress = adress #GPS ???
        self.phone_no = phone_no
        self.opening_hours = opening_hours

hospitals = []



#Event, dass beim Verbindungsaufbau aufgerufen wird
def on_connect(client, userdata, flags, rc):
    client.subscribe([                    
                    ("hshl/hospitals/hospital_1", 2),
                    ])
    
#Event, dass beim Eintreffen einer Nachricht aufgerufen wird
def on_message(client, userdata, msg): #??
    print(str(msg.payload)) #??

#Konstruktor    
client = mqtt.Client() 
client.on_connect = on_connect #Zuweisen des Connect Events
client.on_message = on_message #Zuweisen des Message Events
client.username_pw_set("solace-cloud-client", "nbsse0pkvpkvhpeh3ll5j7rpha") # Benutzernamen und Passwort zur Verbindung setzen
client.connect("mr2mbqbl71a4vf.messaging.solace.cloud", port = 20614) #Verbindung zum Broker aufbauen


data = {
    "name": "Hospital 1", 
    "adress":["Hospital Street", "No.1", "59555 Lippstadt"], #phone no.,...
    "phone_no":["02941-11111"],
    "opening_hours":["Monday - Friday 8.00a.m. until 6.30p.m.", "Saturday - Sunday 8.00a.m. until 6.p.m."],
    "topic": "hshl/hospitals/hospital_1"
    }
client.publish("hshl/server/hospital", json.dumps(data))#?? was bedeutet json.dumps(data)

client.loop_forever()
