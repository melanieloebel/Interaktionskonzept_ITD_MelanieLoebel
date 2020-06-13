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
        print('\n')
        print('List of doctors and their specialistic field: ')
        
        for doc in self.doctors:
            print(doc)
        #print(self.doctors)
        #represent_doctors = '\n'.join(str(self.doctors))
        #print(represent_doctors)

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
                print('DUMM! Try it again!')

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
            if chosen_weekday == 'Saturday' or chosen_weekday == 'Sunday':
                print(
                    'You have chosen a weekend. Please enter another date (DD.MM.YYYY):')
            else:
                print('You have chosen a ',
                      calendar.day_name[request.weekday()])
                break
        
        # Check if the chosen date has free times
        appointment_calendar = {}
        saved_date = request.strftime('%d.%m.%Y')

        possible_times = []
        saved_times = []
        
        #available_times = list(set(possible_times)-set(appointment_calendar.get(saved_date)))

        # Save the available times of the respective doctor in to possible times
        for time in selected_doctor.availability:
            possible_times.append(time)
            #print(time.strftime("%H:%M"))

            # Check if times are available for the chosen date 
            for saved_date in appointment_calendar:
                available_times = list(set(possible_times)-set(appointment_calendar.get(saved_date)))
                if len(available_times) > 0:
                    for time in available_times:
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
                                saved_time = time_obj.strftime('%H:%M')
                                saved_times.append(saved_time)
                                appointment = {doctor : (patient, saved_date, saved_time)}
                                self.appointments.append(appointment)
                                appointment_calendar[saved_date] = saved_time
                                #print('Appointment accepted:')
                    return possible_times
            
                else:
                    print('No appointment available for this date! Please choose another date: ') 
             
           
        
        #counter_possible_times = len(appointment_calendar.get(saved_date))

        #for request in appointment_calendar:
            #for time in selected_doctor.availability:
                #possible_times.append(time)
                #print(time.strftime("%H:%M"))

        #for saved_date in appointment_calendar:
            #if counter_possible_times > 0:
                #possible_times = list(set(possible_times)-set(saved_times))
                #for time in selected_doctor.availability:
                    #print(time.strftime("%H:%M"))

                    # Time input for appointment
                    #validTime = False

                    #while not validTime:
                        #print('Please enter a time of following (HH:MM): ')
                        #timeInput = input()
                        # '08:00'
                        #spl = timeInput.split(':')
                        #time_obj = datetime.time(int(spl[0]), int(spl[1]))
                        #if time_obj in possible_times:
                            #validTime = True
                            #saved_time = time_obj.strftime('%H:%M')
                            #saved_times.append(saved_time)
                            #appointment = {doctor : (patient, saved_date, saved_time)}
                            #self.appointments.append(appointment)
                            #print('Appointment accepted:')
                #return possible_times

                
            #else:
                #print('No appointment available for this date! Please choose another date: ')
        
        
        #for time in selected_doctor.availability:
                #possible_times.append(time)
                #print(time.strftime("%H:%M"))      

        

        # Time input for appointment
        #validTime = False

        #while not validTime:
            #print('Please enter a time of following (HH:MM): ')
            #timeInput = input()
            # '08:00'
            #spl = timeInput.split(':')
            #time_obj = datetime.time(int(spl[0]), int(spl[1]))
            #if time_obj in possible_times:
                #validTime = True
                #print('Appointment accepted:')
                #possible_times.remove(time_obj)
                
                #saved_date = request.strftime('%d.%m.%Y')
                #saved_time = time_obj.strftime('%H:%M')

                #appointment = {doctor : (patient, saved_date, saved_time)}

                #saved_times.append(saved_time)
                #possible_times = list(set(possible_times)-set(saved_times))

                #doc_calendar[saved_date] = saved_time

                #self.appointments.append(appointment)
                #return possible_times

                


        # print(self.appointments)
        print('Appointment accepted:') 
        print(appointment)

    def show_appointments(self):
        print(self.appointments)

    def send_data_to_server(self):
        hospital_info = self.get_hospital_info()
        print('will send this line to the server:')
        print(hospital_info)
        self.communication.send_message(hospital_info)

    # Lukas needs info like this
    #"HospitalMcBrokenFinger 56.2296756,5.0122287 12 hops5 123 einExpter,Nocheiner,UndNochEiner"
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

        doctor4 = Doctor('Dr.',
                         'Sarah Altmann',
                         ['general', 'orthopaedist'],
                         '+49 159 05251 3333',
                         calendar.morning)
        doctorList.append(doctor4)

        doctor5 = Doctor('Dr.',
                         'Tobias Knippschild',
                         ['general', 'internist'],
                         '+49 159 05251 4444',
                         calendar.morning + calendar.afternoon)
        doctorList.append(doctor5)
        
        return [doctor1, doctor2, doctor3, doctor4, doctor5]
        
