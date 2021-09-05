import cv2


def video_demo():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    i = 0
    photoname = 1

    while True:
        i = i + 1
        reg, frame = cap.read()
        frame = cv2.flip(frame, 1)
        #cv2.imshow('windows', frame)

        if i == 50:
            filename = str(photoname) + '.png'
            cv2.imwrite('C:/Users/Administrator/Desktop' + '\\' + filename, frame)
            print(filename + '保存成功')
            i = 0

            photoname = photoname + 1
            if photoname >= 3:
                break
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()


video_demo()
cv2.destroyAllWindows()
