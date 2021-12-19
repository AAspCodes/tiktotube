# Import everything needed to edit video clips
from typing import Concatenate

from moviepy.editor import concatenate_videoclips
from moviepy.editor import VideoFileClip
from rich.traceback import install as ad_fancy_traceback

ad_fancy_traceback()

# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clip = VideoFileClip("sample-mp4-file.mp4").subclip(10, 20)
clip2 = VideoFileClip("sample-mp4-file.mp4").subclip(15, 40)


# concatenate video clips
video = concatenate_videoclips([clip, clip2])

# Write the result to a file (many options available !)
video.write_videofile("new_concated_video.mp4")


# check the link for more information
# https://www.section.io/engineering-education/video-editing-python-moviepy/
