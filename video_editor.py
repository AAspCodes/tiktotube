# Import everything needed to edit video clips
import os

from moviepy.editor import concatenate_videoclips
from moviepy.editor import VideoFileClip
from rich.traceback import install as ad_fancy_traceback

ad_fancy_traceback()
PATH_TO_DOWNLOADED_VIDEOS = "./downloaded_videos/"


def get_video_paths():
    ## Yurii you may need to modfy something do work on windows
    videos = os.listdir(PATH_TO_DOWNLOADED_VIDEOS)
    video_paths = [PATH_TO_DOWNLOADED_VIDEOS + vid for vid in videos]
    return video_paths


def concatenate_videos(video_paths):
    # Load videos
    clips = [VideoFileClip(vid) for vid in video_paths]

    # concatenate video clips
    video = concatenate_videoclips(clips)

    # Write the result to a file (many options available !)
    video.write_videofile("final_video.mp4")


def delete_old_videos():
    for old_video in os.listdir(PATH_TO_DOWNLOADED_VIDEOS):
        os.remove(os.path.join(PATH_TO_DOWNLOADED_VIDEOS, old_video))


# check the link for more information
# https://www.section.io/engineering-education/video-editing-python-moviepy/


if __name__ == "__main__":
    video_paths = get_video_paths()
    concatenate_videos(video_paths)
    delete_old_videos()
