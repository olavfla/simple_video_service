import time
import cv2
import base64
import numpy as np

from middleware.middlewareAPI import *

class VideoReceiver():
    def __init__(self, address, port, hostname):
        self.address = address
        self.port = port
        self.buffer_size = 65536
        self.socket = None
        self.connection = None
        self.client_id = hostname

    def init(self):
        self.socket = MiddlewareReliable()
        self.socket.bind((self.address, self.port))
        self.socket.listen()

    def decode_video(self, packet):
        decoded = base64.b64decode(packet,' /')
        data = np.fromstring(decoded,dtype=np.uint8)
        frame = cv2.imdecode(data,1)

        return frame

    def listen(self):        
        while True:
            if self.connection is None:
                self.connection, addr = self.socket.accept()
            
            packet = self.connection.recv(self.buffer_size)
            frame = self.decode_video(packet)

            if frame is not None:
                cv2.imshow("RECEIVING VIDEO", frame)
            cv2.waitKey(1)

