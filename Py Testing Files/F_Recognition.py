import cv2
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

camera = cv2.VideoCapture(1)

while True:
    ret, img = camera.read()

    faceFrame = face_recognition.face_locations(img)
    encodedFrame = face_recognition.face_encodings(img, faceFrame)

    for encodeFace, locationFace in zip(encodedFrame, faceFrame):
        faceMatch = face_recognition.compare_faces(studentsEncoding, encodeFace, tolerance)

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
    cv2.waitKey(1)
