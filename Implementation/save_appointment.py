import datetime
import calendar
import locale
 
#locale.setlocale(locale.LC_ALL, 'deu_deu')

#Appointment calendar
appointment_calendar = []

#Input patient  
print('Please enter your name: ')
patient = input()

#Input request date for appointment
print('Hello ',patient,',')
print('please enter your appointment whish (DD.MM.YYYY):')

we = True 

while we:
    request_date = input()
 
    #in Datumformat konvertieren
    request = datetime.datetime.strptime(request_date,'%d.%m.%Y').date()

    chosen_weekday = calendar.day_name[request.weekday()]

    if chosen_weekday == 'Saturday' or chosen_weekday == 'Sunday':
        print ('You have chosen a weekend. Please enter another date (DD.MM.YYYY):')

    else:
        print('You have chosen a ',calendar.day_name[request.weekday()])
        break


print(request)

#Possible times
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

#save all times in a list        
possibleTimes = [t1,t2,t5,t6,t15,t17]

#Output times
for time in possibleTimes:
    print(time.strftime("%H:%M"))

#Method time input
validTime = False

while not validTime:
    print('Please enter a time of following (HH:MM): ')
    timeInput = input()
    #'08:00'
    spl = timeInput.split(':')
    time_obj = datetime.time(int(spl[0]), int(spl[1]))
    if time_obj in possibleTimes:
        validTime = True
        print('Appointment accepted:')
        possibleTimes.remove(time_obj)
        appointment = (patient, request.strftime('%d.%m.%Y'), time_obj.strftime('%H:%M'))
        appointment_calendar.append(appointment)
                   
 
print(appointment_calendar)

