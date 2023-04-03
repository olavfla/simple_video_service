import threading

from video_sender import VideoSender

if __name__ == "__main__":
    try:
        dest_address = "192.168.3.10"
        dest_port = 5001
        host_name = "video_sender"

        # Set event to run and close socket thread
        run_event = threading.Event()
        run_event.set()

        camera_port = 2

        sender = VideoSender(dest_address, dest_port, host_name, run_event, camera_port)
        sender.connect()
        sender.start()

    except Exception as e:
        print(e)
        run_event.clear()
        sender.join()