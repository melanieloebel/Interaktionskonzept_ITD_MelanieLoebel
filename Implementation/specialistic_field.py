import paho.mqtt.client as mqtt
import json

class Specialistic_Field:
    def __init__(self, name, floor, free_rooms):
        self.name = name
        self.floor = floor
        self.free_rooms = free_rooms

specialistic_field = []
