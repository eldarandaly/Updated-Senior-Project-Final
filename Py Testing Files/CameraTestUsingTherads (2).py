import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import cv2
import os
from PyQt5.uic import loadUi ,loadUiType
import cv2
import numpy
import face_recognition
import os
from datetime import datetime

path = os.listdir('knownPersons')
tolerance = 0.6
model = 'hog' # Can be 'cnn'
studentsNames = []
images = []
studentsEncoding = []

print(path)

print('Loading and processing faces...')
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


print('Processing Done.')

class MW(QDialog):
    def __init__(self):
        super(MW, self).__init__()
        loadUi("D:/TesingNewProject Bary's Idea/TestingBaryIdea/TestingDailogIdea/TrainTest.ui",self)   

       # self.pushButton.clicked.connect()

        self.Worker1 = Worker1()

        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        #self.setLayout(self.VBL)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

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
    def run(self):
        self.ThreadActive = True
        Capture = cv2.VideoCapture(1)
        while self.ThreadActive:
            ret, Image = Capture.read()
            faceFrame = face_recognition.face_locations(Image)
            encodedFrame = face_recognition.face_encodings(Image, faceFrame)

            for encodeFace, locationFace in zip(encodedFrame, faceFrame):
                self.faceMatch = face_recognition.compare_faces(studentsEncoding, encodeFace, tolerance)

                faceDistance = face_recognition.face_distance(studentsEncoding, encodeFace)
                print(faceDistance)
                matchIndex = numpy.argmin(faceDistance)

               # Image = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
            if self.faceMatch[matchIndex]:
                name = studentsNames[matchIndex].upper()
                print(name)
                top, right, bottom, left = locationFace
                cv2.rectangle(Image, (left,top), (right,bottom), (0,255,0), 2)
                cv2.rectangle(Image, (left, bottom - 35), (right,bottom), (0,255,0), cv2.FILLED)
                cv2.putText(Image, name, (left+6, bottom-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)
                #self.ImageUpdate.emit(Pic)
                cv2.imshow('Face Recognition', Image)
                #cv2.waitKey(1)
                
                

    def stop(self):
        self.ThreadActive = False
        self.quit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MW()
    Root.show()
    sys.exit(App.exec())