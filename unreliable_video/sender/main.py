import threading

from video_sender import VideoSender

from middleware.middlewareAPI import *

if __name__ == "__main__":
    try:
        dest_address = "192.168.3.10"
        dest_port = 5002
        middleware = MiddlewareUnreliable()
        host_name = "video_sender"

        # Set event to run and close socket thread
        run_event = threading.Event()
        run_event.set()

        camera_port = 2

        sender = VideoSender(dest_address, dest_port, middleware, host_name, run_event, camera_port)

        sender.start()
    except Exception as e:
        print(e)
        run_event.clear()
        sender.join()