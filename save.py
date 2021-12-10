import cv2


class VideoCameraSave(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def newMember(self, name):
        ret, frame = self.video.read()
        img_counter = 0
        img_name = name + ".png"
        faces = self.face_cascade.detectMultiScale(frame, 1.3, 5)
        flag = 1
        while True:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (67, 67, 67), 1) #draw rectangle to main image
                detected_face = frame[int(y):int(y+h), int(x):int(x+w)] #crop detected face
                detected_face = cv2.resize(detected_face, (160, 160)) #resize to 224x224
                flag = 0
            if flag == 0:
                cv2.imwrite("./images_db/reg/" + img_name, detected_face)
                print("{} written!".format(img_name))
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
    
class VideoCameraLoginSave(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def newMember(self, name):
        ret, frame = self.video.read()
        img_counter = 0
        img_name = name + ".png"
        faces = self.face_cascade.detectMultiScale(frame, 1.3, 5)
        flag = 1
        while True:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (67, 67, 67), 1) #draw rectangle to main image
                detected_face = frame[int(y):int(y+h), int(x):int(x+w)] #crop detected face
                detected_face = cv2.resize(detected_face, (160, 160)) #resize to 224x224
                flag = 0
            if flag == 0:
                cv2.imwrite("./images_db/logged/" + img_name, detected_face)
                print("{} written!".format(img_name))
            ret, jpeg = cv2.imencode('.jpg', frame)
            return jpeg.tobytes()
