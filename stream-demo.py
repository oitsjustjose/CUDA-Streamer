from flask_opencv_streamer.streamer import Streamer

from ffmpeg import CUDAStreamer

def main() -> None:
    """
    The main launcher logic, using a cuda streamer to stream from an IP camera

    Arguments:
        None
    Returns:
        None
    """

    cuda_streamer = CUDAStreamer("rtsp://consumer:IyKv4uY7%g^8@10.199.51.222/axis-media/media.amp?streamprofile=H264-OpenCV-Optimized", 1920, 1080)
    streamer = Streamer(3030, False, (1920, 1080), frame_rate=30)

    while True:
        frame = cuda_streamer.get_image()
        streamer.update_frame(frame)
        if not streamer.is_streaming:
            streamer.start_streaming()

if __name__ == "__main__":
    main()
