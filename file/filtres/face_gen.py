import cv2
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))
import db as db_f

db_f.creat_databese("../DataBase/database.db")
db = db_f.Database("../DataBase/database.db")

if db.all_user_id() == []:
    id = 0
else:
    id = db.all_user_id()[-1][0] + 1

first_name = input("Введите Фамилию: ")
last_name = input("Введите Имя: ")

print (f"Будет создан пользователь в БД:\nID - {id}\tFirst_name - {first_name}\tLast_name - {last_name}")
db.user_login(id, first_name, last_name)
if db.info_user(id) == None:
    exit()


path = os.path.dirname(os.path.abspath(__file__))
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

i = 0 # Счетчик изображений
maxs = 50 #Кол-во фото (будет в 2 раза больше)
offset = 50 # Расстояние от лица до рамки

name = str(id)

video = cv2.VideoCapture(0) # Camera

while True:
    ret, im = video.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100))

    for (x, y, w, h) in faces:
        i = i+1
        cv2.imwrite("dataSet/face-"+name+"."+str(i)+".jpg", gray[y-offset:y+h+offset, x-offset:x+w+offset])
        cv2.rectangle(im, (x-50, y-50), (x+w+50, y+h+50), (255, 0, 0), 2)
        cv2.imshow('im', im[y-offset:y+h+offset, x-offset:x+w+offset])
        cv2.waitKey(100)
    
    
    if i>=maxs: #Кол-Во Фото
        break

while True:
    ret, im = video.read()
    im = cv2.flip(im, 1)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100))

    for (x, y, w, h) in faces:
        i = i+1
        cv2.imwrite("dataSet/face-"+name+"."+str(i)+".jpg", gray[y-offset:y+h+offset, x-offset:x+w+offset])
        cv2.rectangle(im, (x-50, y-50), (x+w+50, y+h+50), (255, 0, 0), 2)
        cv2.imshow('im', im[y-offset:y+h+offset, x-offset:x+w+offset])
        cv2.waitKey(100)
    
    
    if i>=maxs*2: #Кол-Во Фото
        video.release()
        cv2.destroyAllWindows()
        break
print("Успешно!")