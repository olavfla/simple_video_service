import time
import cv2
import base64
import numpy as np

from middleware.middlewareAPI import *

class VideoReceiver():
    def __init__(self, address, port, hostname):
        self.address = address
        self.port = port
        self.socket = None        
        self.client_id = hostname

    def init(self):
        self.socket = MiddlewareUnreliable()
        self.socket.bind((self.address, self.port))

    def decode_video(self, packet):
        data = base64.b64decode(packet,' /')
        np_data = np.fromstring(data,dtype=np.uint8)
        frame = cv2.imdecode(np_data,1)

        return frame

    def listen(self):        
        while True:
            packet = self.socket.recvfrom()[0]
            frame = self.decode_video(packet)
            
            cv2.imshow("RECEIVING VIDEO", frame)
            cv2.waitKey(1)

