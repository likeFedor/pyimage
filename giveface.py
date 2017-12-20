import cv2
import dlib
from subprocess import call
from time import time

FREQ=5
dlib.get_frontal_face_detector()
def notify(text,title):
    cmd=r'display notification"%s" with title "%s"'%(text,title)
    call(["osascript","-e",cmd])
if __name__=='__main__':
#init videocapture
    cap=cv2.VideoCapure(0)
    cv2.namedWindow('face')
    notify_time=0
    while True:
        #get a frame
        ret,frame=cap.read()
        frame=cv2.resize(frame,(320,240))
        #get face
        faces=FACE_DETECTOR(frame,1)
        for face in faces:
            fimg=frame[face.top():face.bottom(),face.left():face.right()]
            cv2.rectangle(frame,(face.left(),face.top()),(face.right(),face.bottom()),(255,0,0),3)
            #������һ�뷢һ������
            if time()-notify_time>FREQ:
                notify(u'face',u'care')
                notify_time=time()
            cv2.waitKey(500)&0xff==ord('q')
            break
    cv2.destroyAllWindows()
    cap.release()
