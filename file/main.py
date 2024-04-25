import cv2
import os
import DataBase.db as db_f
db_f.creat_databese("DataBase/database.db")
db = db_f.Database("DataBase/database.db")

if os.access("filtres/trainer/trainer.yml", os.F_OK) == False:
    print("Нет Тренировочного файла!\nСначало обучите модель")
    exit()



def face_captur():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('filtres/trainer/trainer.yml')

    cascade_patch = 'filtres/haarcascade_frontalface_default.xml'

    clf = cv2.CascadeClassifier(cascade_patch)
    camera = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_COMPLEX

    while True:
        _, frame = camera.read()
        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = clf.detectMultiScale(
            gray,
            scaleFactor=1.1, #1.1
            minNeighbors=5, #5
            minSize=(100, 100),# 100 100 30 30
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for(x, y, width, height) in face:
            nbr_predicted, coord = recognizer.predict(gray[y:y+height, x:x+width])
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)
            # если нашли пользователя
            
            user = db.info_user(nbr_predicted)
            try:
                nbr_predicted = f'{user[2]} {user[3]}'
            except:
                nbr_predicted = 'Error'
            
            cv2.putText(frame, str(nbr_predicted), (x, y+height+25), font, 1.1, (0, 255, 0))

        cv2.imshow('faces', frame) 

        if cv2.waitKey(1) == ord('q'):
            break
    
    camera.release()
    cv2.destroyAllWindows()


def main():
    face_captur()


if __name__ == '__main__':
    main()