import paho.mqtt.client as mqtt
import json                         # for using json data exchange
import time                         # for using the function make_appointment with date and time input

class Communication:

    def __init__(self, my_id):
        self.id = my_id
        self.server_topic = '/hshl/hospitals/'
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect #assign the Connect Event
        self.client.on_message = self.on_message #assign the Message Event

        self.client.username_pw_set("solace-cloud-client", "nbsse0pkvpkvhpeh3ll5j7rpha") # user name and password for connection

        self.client.connect("mr2mbqbl71a4vf.messaging.solace.cloud", port = 20614) #Establishing a connection to the broker

        self.client.loop_start()
        #self.client.loop_forever()

    def send_message(self, message):
        self.client.publish(
            self.server_topic,
            json.dumps(message)
        )

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe([
                        ("hshl/hospitals/{}".format(self.id), 2),
                        ])

    def on_message(self, client, userdata, msg):
        print(str(msg.payload))
    

