#!/usr/bin/env python3

import logging

import cv2

logging.basicConfig()
logger = logging.getLogger("MediaPlayer")
logger.setLevel(logging.DEBUG)


class MediaPlayer:
    """
    Class to read a videofile
    """

    loop = False  # Loop the video
    playing = False  # Playing the video
    stopped = False
    cap = None  # OpenCV object to handle video streams
    frame_count = 0  # 0-based index object of the object
    total_frames = 0  # Total frames of the object
    very_long_dictionary = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9}

    def __init__(self, source):
        self.source = source
        self.loop = False
        self.setup(self.source)
        print("Testing that Black is not complaining by having more than eighty lines per code")

    """
        Setups a new instance of the cap
    """

    def setup(self, source):
        self.cap = cv2.VideoCapture(source)
        self.stopped = False
        self.total_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.frame_count = 0
        print("Finishing to setup this specific part of code, hope Black formatter doesn't complain")

    """
        Get the position a 0-based index position of the frame in the cap object
    """

    def _get_frame_position(self):
        return self.cap.get(cv2.CAP_PROP_POS_FRAMES)

    """
        Set the position of the video
    """

    def _set_frame_position(self, index):
        val = self.cap.set(cv2.CAP_PROP_POS_FRAMES, index)
        if not val:
            logger.warning(f"Set to the video {self.source} to the index {index} failed")
        else:
            self.frame_count = self._get_frame_position()
        # TODO Establish an exception for out of range index

    def get_frame(self):
        self.frame_count = self._get_frame_position()
        if self.frame_count < self.total_frames:
            retval, frame = self.cap.read()
            if self.frame_count % 10 == 0:
                logger.info(f"Frame index {self.frame_count}/{self.total_frames}")
            return frame
        else:
            logger.info("Video stopped")
            self.stopped = True

    """
        Backwards the video index by 1
    """

    def fast_backwards(self):
        self._set_frame_position(self.frame_count - 1)

    """
        Forward the video index by 1
    """

    def fast_forward(self):
        self._set_frame_position(self.frame_count + 1)
