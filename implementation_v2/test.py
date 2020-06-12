import json

doc_options = {}

class Doc():
    #doc_options = {}
    
    def __init__(self, name, fachgebiet):
        self.name = name
        self.fachgebiet = fachgebiet

    

dok1 = Doc('Klaus','Herz')
dok2 = Doc('Robert','Lunge')
dok3 = Doc('Fabian','wat weiß ich')
print(dok1.name)

dokList=[]
dokList.append(dok1)
dokList.append(dok2)
dokList.append(dok3)

n=1

for d in dokList:
    docName = d
    doc_options[n]=d.name,'specialist for: ',d.fachgebiet
    n=n+1
    #return n

print (doc_options)
print (len(dokList))

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x) 

