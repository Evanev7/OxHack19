import io, cv2
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import win32api
import numpy as np

credentials = CognitiveServicesCredentials("c8c8240e711641f5b157b8eb37d6c908")
face_client = FaceClient("https://westeurope.api.cognitive.microsoft.com/", credentials=credentials)


def emoDi(prevAngle, faceData):
    if len(faceData) == 0:
        return prevAngle
    else:
        emos = faceData[0].face_attributes.emotion
        happy, sad = emos.happiness, emos.surprise
        newAngle = (prevAngle + (happy - sad)/2)
        return newAngle

angle = 0  
x,y = 680, 540
cap = cv2.VideoCapture(0)

while True:
    retval, image = cap.read()
    retval, buffer = cv2.imencode('.jpg', image)
    image = io.BytesIO(buffer)
    
    try:
        faces = face_client.face.detect_with_stream(image, return_face_attributes=['emotion'])
    except:
        pass

    angle = emoDi(angle, faces)
    dx,dy = (200*np.cos(angle),200*np.sin(angle))
    win32api.SetCursorPos((int(x+dx),int(y+dy)))
    if (win32api.GetAsyncKeyState(27)) != 0:
        cap.release()
        break