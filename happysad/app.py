import io, base64
from flask import Flask, render_template, request, jsonify
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import win32api
import numpy as np

credentials = CognitiveServicesCredentials("c8c8240e711641f5b157b8eb37d6c908")
face_client = FaceClient("https://westeurope.api.cognitive.microsoft.com/", credentials=credentials)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('HTMLfile.html')

def emoDi(prevAngle, json):
    if len(json) == 0:
        return prevAngle
    else:
        emos = json[0].face_attributes.emotion
        happy, sad = emos.happiness, emos.sadness
        newAngle = (prevAngle + (happy - sad)/6)
        return newAngle, (happy-sad)/2

global angle, x, y
angle = 0  
x,y = win32api.GetCursorPos()

@app.route('/loop', methods=['POST'])
def loop():
    global angle, x, y
    body = request.get_json()
    image_bytes = base64.b64decode(body['image_base64'].split(',')[1])
    image = io.BytesIO(image_bytes)
    faces = face_client.face.detect_with_stream(image, return_face_attributes=['emotion'])
    angle,fun = emoDi(angle, faces)
    dx,dy = (200*np.cos(angle),200*np.sin(angle))
    win32api.SetCursorPos((int(x+dx),int(y+dy)))
    x,y = win32api.GetCursorPos()
    x -= dx -(x+dx)%1
    y -= dy -(y+dy)%1
    return jsonify({"fun": fun})