import os
import cv2




# def main():
cam=cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    sframe = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    sframe = sframe[:, :, ::-1]
    cv2.imshow('frame', frame)
    k=cv2.waitKey(10)
    if k == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
    
# if __name__=="__main__":
#     main()