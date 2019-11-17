import io, cv2
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from winsound import Beep
from time import sleep


credentials = CognitiveServicesCredentials("c8c8240e711641f5b157b8eb37d6c908")
face_client = FaceClient("https://westeurope.api.cognitive.microsoft.com/", credentials=credentials)
RPS = ["Rock","Paper","Scissors"]

def choice(face):
    emotions = face.face_attributes.emotion
    m = max(emotions.happiness, emotions.anger, emotions.surprise)
    if m == emotions.happiness: 
        return 0
    elif m == emotions.anger: 
        return 1
    else: 
        return 2

cap = cv2.VideoCapture(0)
faces = []
print("Emotional Rock Paper Scissors: ")
1
for i in range(3):
    Beep(440,500)
    sleep(0.5)
Beep(880,500)
while len(faces) != 2:
    retval, image = cap.read()
    retval, buffer = cv2.imencode('.jpg', image)
    image = io.BytesIO(buffer)
    
    try:
        faces = face_client.face.detect_with_stream(image, return_face_attributes=['emotion'])
    except:
        pass
    print("Incorrect number of faces")
    sleep(5)
    
p1, p2 = faces
if p1.face_rectangle.left < p2.face_rectangle.left:
    p2, p1 = p1, p2
c1, c2 = choice(p1), choice(p2)

if c1 == c2: 
    print("Draw! The left player and the right player both picked",RPS[c1]+"!")
elif (c1 - c2)%3 == 1:
    print(RPS[c1],"beats",RPS[c2]+",","the player on the left wins!")
elif (c1 - c2)%3 == 2:
    print(RPS[c2],"beats",RPS[c1]+",","The player on the right wins!")

cap.release()