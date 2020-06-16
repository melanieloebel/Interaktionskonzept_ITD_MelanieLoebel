from hospital import Hospital
from calendar_times import Calendar_times
from doctor import Doctor

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
name = 'HospitalMcBrokenFinger'
free_rooms = 30
id = 'melanie_hospital_1'
coordinates = '51.7038134,8.7743594'  # Paderborn
coordinates = '51.5078011, 7.3301805'  # Dortmund
doctors = create_doctors()



hospital = Hospital(name, free_rooms, id, coordinates, doctors)

hospital.loop()



