import cv2
import base64
import numpy as np

class VideoReceiver():
    def __init__(self, address, port, mw, hostname):
        self.address = address
        self.port = port
        self.buffer_size = 65536
        self.mw = mw
        self.connection = None
        self.client_id = hostname
        self.packetbuf = b""

    def init(self):
        self.mw.bind((self.address, self.port))
        self.mw.listen()

    def decode_video(self, packet):
        # decoded = base64.b64decode(packet,' /')
        # data = np.fromstring(decoded,dtype=np.uint8)
        # frame = cv2.imdecode(data,1)

        return cv2.imdecode(np.frombuffer(packet, dtype=np.uint8),1)

    def listen(self):        
        while True:
            if self.connection is None:
                self.connection, addr = self.mw.accept()
            
            packet = self.connection.recv(self.buffer_size)
            self.packetbuf += packet
            if packet[-2:] == b'\xff\xd9':
                frame = self.decode_video(self.packetbuf)
                self.packetbuf = b""
            else:
                continue

            if frame is not None:
                cv2.imshow("RECEIVING VIDEO", frame)
            cv2.waitKey(1)

