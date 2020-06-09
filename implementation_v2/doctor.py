import json

class Doctor():

    #Konstruktor
    def __init__(self, title, name, specialist, phoneno, availability):
        self.title = title
        self.name = name
        self.specialist = specialist
        self.phoneno = phoneno
        self.availability = availability

    def __str__(self):
        return json.dumps({
            'title': self.title,
            'name': self.name,
            'specialist':self.specialist,
        })
    
    def __repr__(self):
        return self.__str__()