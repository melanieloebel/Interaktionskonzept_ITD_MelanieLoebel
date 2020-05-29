import paho.mqtt.client as mqtt
import json

class Doctor:
    def __init__(self, title, name, specialist):
        self.title = title
        self.name = name
        self.specialist = specialist


doctors = []

#Event, dass beim Verbindungsaufbau aufgerufen wird
def on_connect(client, userdata, flags, rc):
    client.subscribe([                    
                    ("hshl/hospitals/hospital_1", 2),
                    ])
# muss dieses Event so aufgerufen werden ???
