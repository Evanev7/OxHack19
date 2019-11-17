import random, os, io, base64
#from flask import Flask, render_template, request, jsonify
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import win32api
from time import sleep
import numpy as np
import json as j

#credentials = CognitiveServicesCredentials(os.environ['face_api_key'])
#face_client = FaceClient(os.environ['face_api_endpoint'], credentials=credentials)
credentials = CognitiveServicesCredentials("c8c8240e711641f5b157b8eb37d6c908")
face_client = FaceClient("https://westeurope.api.cognitive.microsoft.com/", credentials=credentials)

emotions = ['anger','contempt','disgust','fear','happiness','sadness','surprise']


def best_emotion(emotion):
    emotions = {}
    emotions['anger'] = emotion.anger
    emotions['contempt'] = emotion.contempt
    emotions['disgust'] = emotion.disgust
    emotions['fear'] = emotion.fear
    emotions['happiness'] = emotion.happiness
    emotions['neutral'] = emotion.neutral
    emotions['sadness'] = emotion.sadness
    emotions['surprise'] = emotion.surprise
    return max(zip(emotions.values(), emotions.keys()))[1]


#app = Flask(__name__)
'''
@app.route('/')
def home():


    return render_template('HTMLfile.html')
'''





def emoDi(prevAngle, json):
    if len(json) == 0:
        return None
    else:
        emos = json[0]["faceAttributes"]["emotion"]
        happy, sad = emos["happiness"], emos["sadness"]
        newAngle = (prevAngle + (happy - sad)/30)
        return newAngle

angle = 0
x, y = win32api.GetCursorPos()    

'''
@app.route('/square/', methods=['POST'])
def square():
	num = float(request.form.get('number', 0))
	square = num ** 2
	data = {'square': square}
	data = jsonify(data)
	return data
'''

#@app.route('/loop',methods=['POST'])
def loop():
    sleep(10)
    while True:
        body = request.get_json()

        image_bytes = base64.b64decode(body['image_base64'].split(',')[1])
        image = io.BytesIO(image_bytes)

        faces = face_client.face.detect_with_stream(image,
                                                    return_face_attributes=['emotion'])

        angle = emoDi(angle, faces)
        #angle += 1/50
        dx,dy = (200*np.cos(angle),200*np.sin(angle))
        win32api.SetCursorPos((int(x+dx),int(y+dy)))
        sleep(0.005)
        x,y = win32api.GetCursorPos()
        x -= dx -(x+dx)%1
        y -= dy -(y+dy)%1
        if (win32api.GetAsyncKeyState(27)) != 0:
            break

loop()
'''
@app.route('/result', methods=['POST'])
def check_results():
    body = request.get_json()
    desired_emotion = body['emotion']

    image_bytes = base64.b64decode(body['image_base64'].split(',')[1])
    image = io.BytesIO(image_bytes)

    faces = face_client.face.detect_with_stream(image,
                                                return_face_attributes=['emotion'])

    if len(faces) == 1:
        detected_emotion = best_emotion(faces[0].face_attributes.emotion)

        if detected_emotion == body['emotion']:
            return jsonify({
                'message': '✅ You won! You showed ' + desired_emotion
            })
        else:
            return jsonify({
                'message': '❌ You failed! You needed to show ' + 
                           desired_emotion + 
                           ' but you showed ' + 
                           detected_emotion
            })
    else:
        return jsonify({
            'message': '☠️ ERROR: No faces detected'
        })
'''
