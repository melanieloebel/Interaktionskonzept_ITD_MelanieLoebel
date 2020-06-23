from hospital import Hospital
from calendar_times import Calendar_times
from doctor import Doctor
import json


def create_doctors():
    calendar = Calendar_times()

    doctor1 = Doctor('Dr.',
                        'Wolfgang Elpart',
                        ['general', 'emergency_doc'],
                        '+49 139 05251 0000',
                        calendar.morning)

    doctor2 = Doctor('Dr.',
                        'Silvia Krogull',
                        ['general', 'cardiosurgery'],
                        '+49 139 05251 1111',
                        calendar.morning + calendar.afternoon)

    doctor3 = Doctor('Dr.',
                        'Achim Röttinger',
                        ['general', 'orthopedist'],
                        '+49 139 05251 2222',
                        calendar.afternoon)

    doctor4 = Doctor('Dr.',
                        'Christian Koerdt',
                        ['general', 'dermatological_surgeon'],
                        '+49 139 05251 3333',
                        calendar.morning)

    doctor5 = Doctor('Dr.',
                        'Katja Müllermeier',
                        ['general', 'ophthalmologist'],
                        '+49 139 05251 4444',
                        calendar.morning + calendar.afternoon)

    return [doctor1, doctor2, doctor3, doctor4, doctor5]

#Data for hospital 3
name = 'EVK_Lippstadt'
free_rooms = 20
id = 'mel_hosp3'
coordinates = '51.68474578857422,8.34333610534668'  # Lippstadt
doctors = create_doctors()

hospital = Hospital(name, free_rooms, id, coordinates, doctors)

hospital.loop()