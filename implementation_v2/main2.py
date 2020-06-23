from hospital import Hospital
from calendar_times import Calendar_times
from doctor import Doctor
import json


def create_doctors():
    calendar = Calendar_times()

    doctor1 = Doctor('Dr.',
                        'Renata Silverstone',
                        ['general', 'cardiosurgery'],
                        '+49 169 05251 0000',
                        calendar.morning)

    doctor2 = Doctor('Dr.',
                        'Maria Wegener',
                        ['general', 'dermatological_surgeon'],
                        '+49 169 05251 1111',
                        calendar.morning + calendar.afternoon)

    doctor3 = Doctor('Dr.',
                        'Greta Koopmann',
                        ['general', 'orthopedist'],
                        '+49 169 05251 2222',
                        calendar.afternoon)

    doctor4 = Doctor('Dr.',
                        'Christian Gösling',
                        ['general', 'neurologist'],
                        '+49 169 05251 3333',
                        calendar.morning)

    doctor5 = Doctor('Dr.',
                        'Viktor Kratchnisky',
                        ['general', 'emergency_doc'],
                        '+49 169 05251 4444',
                        calendar.morning + calendar.afternoon)

    return [doctor1, doctor2, doctor3, doctor4, doctor5]

#Data for hospital 2
name = 'St_Johannes_Hospital'
free_rooms = 75
id = 'mel_hosp2'
coordinates = '51.51,7.45'  # Dortmund
doctors = create_doctors()

hospital = Hospital(name, free_rooms, id, coordinates, doctors)

hospital.loop()