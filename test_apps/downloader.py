import os
from urllib.request import urlretrieve

url = ("https://twitter.com/i/status/1717495322237354013")

vid_file = "test_video.mp4"

urlretrieve(url, vid_file)

