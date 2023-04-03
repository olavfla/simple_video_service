from video_receiver import VideoReceiver

if __name__ == "__main__":
    receiver = VideoReceiver("0.0.0.0", 5001, "video_receiver")
    receiver.init()
    receiver.listen()