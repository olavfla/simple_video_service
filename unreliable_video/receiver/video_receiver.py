import cv2
import base64
import numpy as np

class VideoReceiver():
    def __init__(self, address, port, mw, hostname):
        self.address = address
        self.port = port
        self.mw = mw        
        self.client_id = hostname

    def init(self):
        self.mw.bind((self.address, self.port))

    def decode_video(self, packet):
        data = base64.b64decode(packet,' /')
        np_data = np.fromstring(data,dtype=np.uint8)
        frame = cv2.imdecode(np_data,1)

        return frame

    def listen(self):        
        while True:
            packet = self.mw.recvfrom()[0]
            frame = self.decode_video(packet)
            
            cv2.imshow("RECEIVING VIDEO", frame)
            cv2.waitKey(1)

