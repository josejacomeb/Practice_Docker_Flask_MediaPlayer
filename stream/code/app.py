#!/usr/bin/env python3

import logging
import os

from stream import MediaPlayer

logging.basicConfig()
logger = logging.getLogger("MediaPlayer")
logger.setLevel(logging.DEBUG)

videos_dir = os.getenv("DOCKER_VIDEO_FOLDER")
print("Hello there this is a simple test to check how superlinter works, hope everything is correct")
files = os.listdir(videos_dir)


def main():
    for file in files:
        if ".mkv" in file or ".mp4" in file:
            stream = MediaPlayer(os.path.join(videos_dir, file))
            while not stream.stopped:
                stream.get_frame()


if __name__ == "__main__":
    main()
