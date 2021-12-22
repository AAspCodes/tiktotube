import os
from typing import Generator

from moviepy.editor import CompositeVideoClip
from moviepy.editor import concatenate_videoclips
from moviepy.editor import ImageClip
from moviepy.editor import VideoFileClip
from moviepy.video.VideoClip import VideoClip
from rich.traceback import install as ad_fancy_traceback

ad_fancy_traceback()


class VideoEditor:
    def __init__(
        self,
        keep_old_vids=True,
        output_vid_name="final_video.mp4",
        path_to_dloaded_vids="downloaded_videos",
        path_to_background_image="background_image.jpg",
    ) -> None:
        self.keep_old_vids = keep_old_vids
        self.output_vid_name = output_vid_name
        self.path_to_dloaded_vids = path_to_dloaded_vids
        self.path_to_background_image = path_to_background_image

    def edit(self) -> None:
        vid_paths = self.get_video_paths()
        videos = self.load_videos(vid_paths)
        video = concatenate_videoclips(videos)
        video = self.add_background_image(video)
        self.write_video(video)

        if not self.keep_old_vids:
            self.delete_saved_videos()

    def get_video_paths(self) -> Generator:
        vids = os.listdir(self.path_to_dloaded_vids)
        return (os.path.join(self.path_to_dloaded_vids, vid) for vid in vids)

    def load_videos(self, vid_paths: Generator) -> list:
        return [VideoFileClip(vid, target_resolution=(1440, 810)) for vid in vid_paths]

    def add_background_image(self, video: VideoClip) -> CompositeVideoClip:
        # load image and specify the image should last the full length of the video
        background_image = ImageClip(self.path_to_background_image).set_duration(
            video.duration
        )

        # add background image
        return CompositeVideoClip([background_image, video.set_pos("center")])

    def write_video(self, video: CompositeVideoClip) -> None:
        # Write the result to a file
        video.write_videofile(self.output_vid_name, audio_codec="aac")

    def delete_old_vids(self) -> None:
        for old_video in os.listdir(self.path_to_dloaded_vids):
            os.remove(os.path.join(self.path_to_dloaded_vids, old_video))


# check the link for more information
# https://www.section.io/engineering-education/video-editing-python-moviepy/


if __name__ == "__main__":
    VideoEditor().edit()
