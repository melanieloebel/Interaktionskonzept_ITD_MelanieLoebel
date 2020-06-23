from hospital import Hospital
from calendar_times import Calendar_times
from doctor import Doctor
import json

def create_doctors():
    calendar = Calendar_times()

    doctor1 = Doctor('Dr.',
                     'Paul Stollmann',
                     ['general', 'cardiosurgery'],
                     '+49 159 05251 0000',
                     calendar.morning)

    doctor2 = Doctor('Dr.',
                     'Maria Anna Weber',
                     ['general', 'orthopedist'],
                     '+49 159 05251 1111',
                     calendar.morning + calendar.afternoon)

    doctor3 = Doctor('Dr.',
                     'Cristina Pardo Trigo',
                     ['general', 'emergency_doc'],
                     '+49 159 05251 2222',
                     calendar.afternoon)

    doctor4 = Doctor('Dr.',
                     'Sarah Altmann',
                     ['general', 'internist'],
                     '+49 159 05251 3333',
                     calendar.morning)

    doctor5 = Doctor('Dr.',
                     'Tobias Knippschild',
                     ['general', 'dermatological_surgeon'],
                     '+49 159 05251 4444',
                     calendar.morning + calendar.afternoon)

    return [doctor1, doctor2, doctor3, doctor4, doctor5]

#Data for hospital 1
name = 'St_Vincenz_Krankenhaus'
free_rooms = 30
id = 'mel_hosp1'
coordinates = [51.71,8.75]  # Paderborn
doctors = create_doctors()

#json.dumps({'name':'St_Vincenz_Krankenhaus', 'free_rooms': '30', 
#'id': 'mel_hosp1', 'coordinates' : [51.71811294555664,8.759356498718261], 
#'doctors' : create_doctors() })

hospital = Hospital(name, free_rooms, id, coordinates, doctors)

hospital.loop()



