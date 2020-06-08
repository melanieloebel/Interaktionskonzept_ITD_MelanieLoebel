import paho.mqtt.client as mqtt
import json

class Hospital:
    def __init__(self, name, address, phone_no, opening_hours, spec_fields, free_rooms, doctors, topic):
        self.name = name
        self.address = address #GPS ???
        self.phone_no = phone_no
        self.opening_hours = opening_hours
        self.spec_fields = spec_fields
        self.free_rooms = free_rooms
        self.doctors = doctors

hospitals = []

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe([
                    ("hshl/server/hospitals/appointment_request", 2), #Topic für Terminanfrage, so ok?
                    ("hshl/server/hospitals", 2), 
                    ])

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if(msg.topic.endswith('hospitals')):
        register_hospital(msg.payload)
    if(msg.topic.endswith('appointment_request')):
        process_appointment_request(msg.payload)

def process_appointment_request(data):
    js = json.loads(data)
    #???
    
    client.publish(topic, response)
 

def register_hospital(data):
    js = json.loads(data)
    hospital = Hospital(js['name'], js['address'], js['phone_no'], js['opening_hours'], js['spec_fields'], js['free_rooms'], js['doctors'], js['topic'])
    hospitals.append(hospital)
    print('#####################')
    for h in hospitals:
        print(h.name)
        print(h.address)
        print(h.phone_no)
        print(h.opening_hours)
        print(h.spec_fields)
        print(h.free_rooms)
        print(h.doctors)
        print('--------------')
    print('#####################')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()