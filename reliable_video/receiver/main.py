from video_receiver import VideoReceiver

from middleware.middlewareAPI import *


if __name__ == "__main__":
    middleware = MiddlewareReliable()
    receiver = VideoReceiver("0.0.0.0", 5001, middleware, "video_receiver")
    receiver.init()
    receiver.listen()