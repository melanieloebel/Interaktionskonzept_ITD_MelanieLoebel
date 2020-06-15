from doctor import Doctor
from calendar_times import Calendar_times
from communication import Communication
import datetime
from datetime import date
import calendar


class Hospital:

    def __init__(self):
        self.name = 'HospitalMcBrokenNose'
        self.doctors = self.create_doctors()
        self.free_rooms = 20
        self.id = 'melanie_hospital_3'
        self.coordinates = '41.2513912,8.2440209'
        self.communication = Communication(self.id)
        self.appointments = {}

    def loop(self):
        options = {
            '1': self.show_doctors,
            '2': self.show_free_rooms,
            '3': self.update_free_rooms,
            '4': self.make_appointment,
            '5': self.show_appointments,
            '6': self.send_data_to_server,
        }
        print('\n')
        print('----------{}-----------'.format(self.name))
        while True:
            #print('Specialistic fields: ', self.get_doctors_specialist())
            print('Select one option:')
            print('1 - show doctors')
            print('2 - show free rooms')
            print('3 - update free rooms')
            print('4 - make an appointment')
            print('5 - show appointments')
            print('6 - send data to the server')

            option = input()
            if(option in options):
                options[option]()
            else:
                print('invalid option')

    def show_doctors(self):
        print('\n')
        print('List of doctors and their specialistic field: ')

        for doc in self.doctors:
            print(doc)
        # print(self.doctors)
        #represent_doctors = '\n'.join(str(self.doctors))
        # print(represent_doctors)

    def show_free_rooms(self):
        print('There are {} free rooms'.format(self.free_rooms))

    def update_free_rooms(self):
        free_rooms = input('Please enter the number of free rooms:')
        self.free_rooms = int(free_rooms)
        self.show_free_rooms()

    def make_appointment(self):

        # Input patient name
        print('Please enter your name: ')
        patient = input()

        # Input Doctor
        doc_options = {}
        print('\n')
        print('Hello ', patient, ',')
        print('please choose one doctor for your appointment wish: ')

        while True:
            count = 1
            for doctor in self.doctors:
                doc_options[count] = doctor
                print('{} - {}'.format(count, doctor))
                count = count + 1

            selected_index = int(input())
            if(selected_index in doc_options):
                selected_doctor = doc_options[selected_index]
                break
            else:
                print('Invalid option! Please try it again!')

        print('You have selected {} {}'.format(
            selected_doctor.title, selected_doctor.name))

        # Input date for appointment wish with check if chosen weekday is a weekend
        print('Please enter your appointment whish (DD.MM.YYYY):')

        validWeekday = True

        while validWeekday:
            request_date = input()
            # in Datumformat konvertieren
            request = datetime.datetime.strptime(
                request_date, '%d.%m.%Y').date()
            chosen_weekday = calendar.day_name[request.weekday()]

            # Today
            #date_today = date.today()
            #date_today = datetime.datetime.strptime(date_today, '%d.%m.%Y').date()

            if chosen_weekday == 'Saturday' or chosen_weekday == 'Sunday':
                print(
                    'You have chosen a weekend. Please enter another date (DD.MM.YYYY):')

            elif request < date.today():
                print('Choose a date from today or in the future: ')

            else:
                print('You have chosen a ',
                      calendar.day_name[request.weekday()])
                break

        # ask for a time slot
        for t in selected_doctor.availability:
            print(t.strftime('%H:%M'))

        validTime = False

        while not validTime:
            print('Please enter a time of following (HH:MM): ')
            timeInput = input()
            # '08:00'
            spl = timeInput.split(':')
            time_obj = datetime.time(int(spl[0]), int(spl[1]))
            if time_obj in selected_doctor.availability:
                saved_time = time_obj.strftime('%H:%M')
                saved_date = request.strftime('%d.%m.%Y')

                # now check if this slot is free for this day
                key = '{}-{}-{}-{}'.format(
                    selected_doctor.title,
                    selected_doctor.name,
                    saved_date,
                    saved_time)

                if key in self.appointments:
                    #possible_times.remove(saved_time)
                    print('This time slot is not free')
                    
                else:
                    validTime = True
                    self.appointments[key] = {patient, saved_date, saved_time}
                    print('Appointment accepted:')
                    print({'{}-{}'.format(selected_doctor.title, selected_doctor.name):(patient, saved_date, saved_time)})
       
    def show_appointments(self):
        print(self.appointments)

    def send_data_to_server(self):
        hospital_info = self.get_hospital_info()
        print('will send this line to the server:')
        print(hospital_info)
        self.communication.send_message(hospital_info)

    def get_hospital_info(self):
        specialists = ', '.join(self.get_doctors_specialist())
        hospital_info = self.name + ' ' + self.coordinates + ' ' + str(len(self.doctors)) + \
            ' ' + self.id + ' ' + str(self.free_rooms) + ' ' + specialists
        return hospital_info

    def get_doctors_specialist(self):
        specialists = []
        for doctor in self.doctors:
            specialists = list(set(doctor.specialist) -
                               set(specialists)) + specialists
        return specialists

    # create Doctor objects that represents the doctors of the hospital
    def create_doctors(self):
        calendar = Calendar_times()

        doctor1 = Doctor('Dr.',
                         'Wolfgang Elpart',
                         ['general', 'internist'],
                         '+49 139 05251 0000',
                         calendar.morning)

        doctor2 = Doctor('Dr.',
                         'Silvia Krogull',
                         ['general', 'gastroenterologist'],
                         '+49 139 05251 1111',
                         calendar.morning + calendar.afternoon)

        doctor3 = Doctor('Dr.',
                         'Achim Röttinger',
                         ['general', 'cardiosurgery'],
                         '+49 139 05251 2222',
                         calendar.afternoon)

        doctor4 = Doctor('Dr.',
                         'Christian Koerdt',
                         ['general', 'pneumologist'],
                         '+49 139 05251 3333',
                         calendar.morning)

        doctor5 = Doctor('Dr.',
                         'Katja Müllermeier',
                         ['general', 'ophthalmologist'],
                         '+49 139 05251 4444',
                         calendar.morning + calendar.afternoon)

        return [doctor1, doctor2, doctor3, doctor4, doctor5]
