from doctor import Doctor
from calendar_times import Calendar_times
from communication import Communication
import datetime
import calendar


class Hospital:

    def __init__(self):
        self.name = 'HospitalMcBrokenFinger'
        self.doctors = self.create_doctors()
        self.free_rooms = 30
        self.id = 'melanie_hospital_1'
        self.coordinates = '51.6813912,8.3420209'
        self.communication = Communication(self.id)
        self.appointments = []

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
        print(self.doctors)

    def show_free_rooms(self):
        print('There are {} free rooms'.format(self.free_rooms))

    def update_free_rooms(self):
        free_rooms = input('Please enter the number of free rooms:')
        self.free_rooms = int(free_rooms)
        self.show_free_rooms()

    def make_appointment(self):
        possible_times = []
        # show possible times
        # for doctor in self.doctors:
        #     print('{} {}'.format(doctor.name, str(doctor.specialist)))
        #     for time in doctor.availability:
        #         possible_times.append(time)
        #         print(time.strftime("%H:%M"))

        print('Please enter your name: ')
        patient = input()

        # Input Doctor
        doc_options = {}
        print('\n')
        print('Hello ', patient, ',')

        # Input request date for appointment
        print('Please enter your appointment whish (DD.MM.YYYY):')

        # Check if chosen weekday is a weekend
        validWeekday = True

        while validWeekday:
            request_date = input()
            # in Datumformat konvertieren
            request = datetime.datetime.strptime(
                request_date, '%d.%m.%Y').date()
            chosen_weekday = calendar.day_name[request.weekday()]
            if chosen_weekday == 'Saturday' or chosen_weekday == 'Sunday':
                print(
                    'You have chosen a weekend. Please enter another date (DD.MM.YYYY):')
            else:
                print('You have chosen a ',
                      calendar.day_name[request.weekday()])
                break

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
                print('DUMM! try it again!')

        print('You have selected {} {}'.format(
            selected_doctor.title, selected_doctor.name))
        for time in selected_doctor.availability:
            possible_times.append(time)
            print(time.strftime("%H:%M"))

        validTime = False

        while not validTime:
            print('Please enter a time of following (HH:MM): ')
            timeInput = input()
            # '08:00'
            spl = timeInput.split(':')
            time_obj = datetime.time(int(spl[0]), int(spl[1]))
            if time_obj in possible_times:
                validTime = True
                print('Appointment accepted:')
                possible_times.remove(time_obj)
                appointment = (patient, request.strftime(
                    '%d.%m.%Y'), time_obj.strftime('%H:%M'))

                self.appointments.append(appointment)
        # print(self.appointments)
        print(appointment)

    def show_appointments(self):
        print(self.appointments)

    def send_data_to_server(self):
        hospital_info = self.get_hospital_info()
        print('will send this line to the server:')
        print(hospital_info)
        self.communication.send_message(hospital_info)

    # Lukas Walter is waiting for the info like this
    #"HospitalMcBrokenFinger 56.2296756,5.0122287 12 hops5 123 einExpter,Nocheiner,UndNochEiner"
    def get_hospital_info(self):
        specialists = ''.join(self.get_doctors_specialist())
        hospital_info = self.name + ' ' + self.coordinates + ' ' + '12' + \
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
        doctorList = []

        doctor1 = Doctor('Dr.',
                         'Paul Stollmann',
                         ['general', 'heart_attack'],
                         '+49 159 05251 0000',
                         calendar.morning)
        doctorList.append(doctor1)

        doctor2 = Doctor('Dr.',
                         'Maria Anna Weber',
                         ['general', 'surgery'],
                         '+49 159 05251 1111',
                         calendar.morning + calendar.afternoon)
        doctorList.append(doctor2)

        doctor3 = Doctor('Dr.',
                         'Cristina Pardo Trigo',
                         ['general', 'neurology'],
                         '+49 159 05251 2222',
                         calendar.afternoon)
        doctorList.append(doctor3)
        
        return [doctor1, doctor2, doctor3]
