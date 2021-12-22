# Import everything needed to edit video clips
import os

from moviepy.editor import concatenate_videoclips
from moviepy.editor import VideoFileClip
from rich.traceback import install as ad_fancy_traceback

ad_fancy_traceback()


class VideoEditor:
    def __init__(
        self,
        keep_old_vids=True,
        output_vid_name="final_video.mp4",
        path_to_dloaded_vids="downloaded_videos",
    ) -> None:
        self.keep_old_vids = keep_old_vids
        self.output_vid_name = output_vid_name
        self.path_to_dloaded_vids = path_to_dloaded_vids

    def edit(self):
        vid_paths = self.get_video_paths()
        self.concatenate_videos(vid_paths)
        if not self.keep_old_vids:
            self.delete_saved_videos()

    def get_video_paths(self):
        ## Yurii you may need to modfy something do work on windows
        videos = os.listdir(self.path_to_dloaded_vids)
        return (os.path.join(self.path_to_dloaded_vids, vid) for vid in videos)

    def concatenate_videos(self, vid_paths):
        # Load videos
        clips = [VideoFileClip(vid) for vid in vid_paths]

        # concatenate video clips
        video = concatenate_videoclips(clips)

        # Write the result to a file
        video.write_videofile(self.output_vid_name, audio_codec="aac")

    def delete_old_vids(self):
        for old_video in os.listdir(self.path_to_dloaded_vids):
            os.remove(os.path.join(self.path_to_dloaded_vids, old_video))


# check the link for more information
# https://www.section.io/engineering-education/video-editing-python-moviepy/


if __name__ == "__main__":
    VideoEditor().edit()
