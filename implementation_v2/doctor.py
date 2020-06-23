import json

class Doctor():

    def __init__(self, title, name, specialist, phoneno, availability):
        self.title = title
        self.name = name
        self.specialist = specialist
        self.phoneno = phoneno
        self.availability = availability

    # method for string return the doctor with its specialist fields 
    def __str__(self):
        return '{} {} \n{}\n'.format(self.title, self.name, self.specialist)
    
    # method for display the doctor with its specialist fields 
    def __repr__(self):
        return self.__str__()