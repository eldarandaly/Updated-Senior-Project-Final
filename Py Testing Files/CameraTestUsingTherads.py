import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import os
from PyQt5.uic import loadUi ,loadUiType
import numpy
import face_recognition
import os
from datetime import datetime


def Attendance(name):
    with open('Attendance.csv','r+') as f:
        attended = f.readlines()
        namesAttended = []
        for line in attended:
            entry = line.split(',')
            namesAttended.append(entry[0])
        if name not in namesAttended:
            attendTime = datetime.now().strftime('%H:%M:%S')
            f.writelines(f'\n{name},{attendTime}')

path = os.listdir('knownPersons')
tolerance = 0.6
model = 'hog' # Can be 'cnn'
studentsNames = []
images = []
studentsEncoding = []

for sName in path:
    print("-------------------------------------")
    print(sName)
    for sImage in os.listdir(f'knownPersons/{sName}'):
        currentPath = f'knownPersons/{sName}/{sImage}'
        print(sImage)
        img = face_recognition.load_image_file(currentPath)
        images.append(img)
        studentsEncoding.append(face_recognition.face_encodings(img)[0])
        studentsNames.append(sName)


'''
class FaceRecogn():
    def model():
        while True:
            ret, img = camera.read()

            faceFrame = face_recognition.face_locations(img)
            encodedFrame = face_recognition.face_encodings(img, faceFrame)

            for encodeFace, locationFace in zip(encodedFrame, faceFrame):
                faceMatch = face_recognition.compare_faces(studentsEncoding, encodeFace,tolerance)

                faceDistance = face_recognition.face_distance(studentsEncoding, encodeFace)
                print(faceDistance)

                matchIndex = numpy.argmin(faceDistance)

                if faceMatch[matchIndex]:
                    name = studentsNames[matchIndex].upper()
                    print(name)
                    top, right, bottom, left = locationFace
                    cv2.rectangle(img, (left,top), (right,bottom), (0,255,0), 2)
                    cv2.rectangle(img, (left, bottom - 35), (right,bottom), (0,255,0), cv2.FILLED)
                    cv2.putText(img, name, (left+6, bottom-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)
                    Attendance(name)

            cv2.imshow('Face Recognition', img)
            cv2.waitKey('q')        
'''


class MW(QDialog):
    def __init__(self):
        super(MW, self).__init__()
        loadUi("D:/TesingNewProject Bary's Idea/TestingBaryIdea/TestingDailogIdea/TrainTest.ui",self)   

       # self.pushButton.clicked.connect()

        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        #self.setLayout(self.VBL)

    def ImageUpdateSlot(self, imgh):
        self.FeedLabel.setPixmap(QPixmap.fromImage(imgh))
        
        #self.FeedLabel.setPixmap(Worker1.model)
    def CancelFeed(self):
        self.Worker1.stop()
        

'''class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.VBL = QVBoxLayout()

        self.FeedLabel = QLabel()
        self.VBL.addWidget(self.FeedLabel)

        self.CancelBTN = QPushButton("Cancel")
        self.CancelBTN.clicked.connect(self.CancelFeed)
        self.VBL.addWidget(self.CancelBTN)

        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.setLayout(self.VBL)

    #def ImageUpdateSlot(self, Image):
     #   self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    #def CancelFeed(self):
    #    self.Worker1.stop()'''

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)

    def testrun(self):
        camera = cv2.VideoCapture(1)
        self.ThreadActive = True

        while self.ThreadActive:

            ret,img=camera.read()
            faceFrame = face_recognition.face_locations(img)
            encodedFrame = face_recognition.face_encodings(img, faceFrame)

            for encodeFace, locationFace in zip(encodedFrame, faceFrame):

                faceMatch = face_recognition.compare_faces(studentsEncoding, encodeFace, tolerance)
                faceDistance = face_recognition.face_distance(studentsEncoding, encodeFace)
                print(faceDistance)

                matchIndex = numpy.argmin(faceDistance)

                if faceMatch[matchIndex] & ret:
                    name = studentsNames[matchIndex].upper()
                    print(name)
                    top, right, bottom, left = locationFace
                    cv2.rectangle(img, (left,top), (right,bottom), (0,255,0), 2)
                    cv2.rectangle(img, (left, bottom - 35), (right,bottom), (0,255,0), cv2.FILLED)
                    cv2.putText(img, name, (left+6, bottom-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)
                    imgh = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    FlippedImage = cv2.flip(imgh, 1)
                    ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                    Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.ImageUpdate.emit(Pic)
                    print("here")
                    #Attendance(name)
        cv2.imshow('Face Recognition',img)
        cv2.waitKey('q')            
    def stop(self):
        self.ThreadActive = False
        self.quit()
    
    '''
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(1)
        while self.ThreadActive:
            ret, frame = Capture.read()
            if ret:
                Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
    def stop(self):
        self.ThreadActive = False
        self.quit()'''
 
if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MW()
    Root.show()
    sys.exit(App.exec())