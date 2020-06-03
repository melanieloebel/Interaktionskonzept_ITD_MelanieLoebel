import paho.mqtt.client as mqtt
import json
import time
import datetime
#import appointment


class Doctor():

    #Konstruktor
    def __init__(self, title, name, specialist, phoneno):
        self.title = title
        self.name = name
        self.specialist = specialist
        self.phoneno = phoneno
        
#possible times which can be chosen
t1 = datetime.time(8,00)
t2 = datetime.time(8,30)
t3 = datetime.time(9,00)
t4 = datetime.time(9,30)
t5 = datetime.time(10,00)
t6 = datetime.time(10,30)
t7 = datetime.time(11,00)
t8 = datetime.time(11,30)
t9 = datetime.time(12,00)
t10 = datetime.time(12,30)

t11 = datetime.time(13,00)
t12 = datetime.time(13,30)
t13 = datetime.time(14,00)
t14 = datetime.time(14,30)
t15 = datetime.time(15,00)
t16 = datetime.time(15,30)
t17 = datetime.time(16,00)
t18 = datetime.time(16,30)
t19 = datetime.time(17,00)
t20 = datetime.time(17,30)

#creation of a list with possible times
possibleTimes= [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12,t13,t14,t15,t16,t17,t18,t19,t20]
calender = []

#Weekday
wdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    #Methode Termin speichern   
    def save_appointment(self):
        
        patient_name = input("Please enter your name: ")
        print (patient_name)

        from datetime import datetime
        request_app_date = datetime.strptime(input ("Please enter your wish appointment in format YYYY-MM-DD: "), "%Y-%m-%d")

        app_date = request_app_date.strftime("%d.%m.%Y")

        print (app_date)








