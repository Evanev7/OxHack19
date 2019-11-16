import math as m
import json as j

sensitivity = 10

def emoDi(prevAngle, json):
    if len(json) == 0:
        return None
    else:
        emos = json[0]["faceAttributes"]["emotion"]
        happy, neutral, sad = emos["happiness"], emos["neutral"], emos["sadness"]
        newAngle = (prevAngle + (happy - sad)) % (2*m.pi)
        return newAngle


"""with open ("example.txt") as file:
    data = j.load(file)
angle = 0
while True:
    angle = emoDi(angle, data)
    print(angle)
    #data = new pic"""


    
    
