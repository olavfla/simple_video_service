from threading import Thread
import time
import cv2
import imutils
import base64

class VideoSender(Thread):
    def __init__(self, address, port, mw, hostname, run_event, camera_port):
        super().__init__()
        self.setDaemon(True)

        self.address = address
        self.port = port
        self.mw = mw
        self.client_id = hostname
        self.run_event = run_event
        self.tos = 88
        self.quality = 40
        self.delay = 0.05

        self.video_capture = cv2.VideoCapture(camera_port)

    def connect(self):
        self.mw.connect((self.address, self.port))
    
    def encode(self, buffer):
        return base64.b64encode(buffer)
    
    def send(self, msg):
        self.mw.sendall(msg)
    
    def start(self):
        while self.run_event.is_set():
            _, frame = self.video_capture.read()
            frame = imutils.resize(frame, width=400)
            _, buffer = cv2.imencode('.jpg',frame,[cv2.IMWRITE_JPEG_QUALITY,self.quality])
            message = buffer #self.encode(buffer)
            self.send(message)
            time.sleep(self.delay)
            
            cv2.waitKey(1)
            

