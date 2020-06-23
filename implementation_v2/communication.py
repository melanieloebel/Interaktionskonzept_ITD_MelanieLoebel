import paho.mqtt.client as mqtt
import json
import time

class Communication:

    def __init__(self, my_id):
        self.id = my_id
        self.server_topic = '/hshl/hospitals/'
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect #Zuweisen des Connect Events
        self.client.on_message = self.on_message #Zuweisen des Message Events

        self.client.username_pw_set("solace-cloud-client", "nbsse0pkvpkvhpeh3ll5j7rpha") # Benutzernamen und Passwort zur Verbindung setzen

        self.client.connect("mr2mbqbl71a4vf.messaging.solace.cloud", port = 20614) #Verbindung zum Broker aufbauen

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
    

