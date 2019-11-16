import json

def emotionToRPS (json_face):
    happiness = json_face["faceAtributes"]["emotion"]["happiness"]
    neutrality = json_face["faceAtributes"]["emotion"]["neutral"]
    anger = json_face["faceAtributes"]["emotion"]["anger"]
    surprise = json_face["faceAtributes"]["emotion"]["surprise"]
    
    if max(happiness, neutrality, anger, surprise) = happiness:
        return "Rock"
    if max(happiness, neutrality, anger, surprise) = anger:
        return "Paper"
    if max(happiness, neutrality, anger, surprise) = surprise:
        return "Scissors"
    if max(happiness, neutrality, anger, surprise) = neutrality:
        return "Nothing"
    
    return "Nothing"
    
    