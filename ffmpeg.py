"""
An FFMPEG wrapper for using CUDA-based streaming

Author: Jose Stovall | stovallj1995@gmail.com | oitsjustjose@git

Center for Urban Informatics and Progress | CUIP | utccuip.com
"""

import subprocess

import cv2
import numpy as np


class CUDAStreamer:
    """
    Uses the natively compiled FFMPEG command to get a CV2 image from RTSP
    Arguments
    """

    def __init__(self, camera_url: str, width: int, height: int):
        self.cmd = subprocess.Popen(
            [
                "ffmpeg",
                "-hide_banner",
                "-loglevel",
                "panic",
                "-hwaccel",
                "nvdec",
                "-reorder_queue_size",
                "10000",
                "-rtsp_transport",
                "tcp",
                "-i",
                camera_url,
                "-vsync",
                "0",
                "-vcodec",
                "h264_nvenc",
                "-f",
                "image2pipe",
                "-pix_fmt",
                "bgr24",
                "-vcodec",
                "rawvideo",
                "-",
            ],
            stdout=subprocess.PIPE,
            bufsize=10,
        )
        self.width = width
        self.height = height

    def get_image(self) -> np.array:
        raw = self.cmd.stdout.read(self.width * self.height * 3)
        image = np.fromstring(raw, dtype="uint8")
        try:
            image = image.reshape((self.height, self.width, 3))
        except ValueError:
            pass
        self.cmd.stdout.flush()
        return image
