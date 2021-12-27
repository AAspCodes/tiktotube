import os
from typing import Dict
from typing import List


class Downloader:
    def __init__(
        self,
        api,
        path_to_dloaded_vids="downloaded_videos",
        video_prefix="saved_video",
    ) -> None:
        self.path_dloaded_vids = path_to_dloaded_vids
        self.video_prefix = video_prefix
        self.api = api

    def download_all(self, vid_dicts: List) -> None:
        self.check_for_dir()

        # loop through and get just the dload addrs
        for index, vid_dict in enumerate(vid_dicts):
            dload_url = self.get_dload_url(vid_dict)
            video_bytes = self._download(dload_url)
            path = self.compute_path(index)
            self.write_video(video_bytes, path)

    def _download(self, dload_url: str) -> bytes:
        return self.api.get_video_by_download_url(dload_url)

    def write_video(self, video_bytes: bytes, path: str) -> None:
        with open(path, "wb") as f:
            f.write(video_bytes)

    def compute_path(self, index: int) -> str:
        return os.path.join(
            self.path_dloaded_vids, self.video_prefix + str(index) + ".mp4"
        )

    def get_dload_url(self, vid_dict: Dict) -> str:
        return vid_dict["video"]["downloadAddr"]

    def check_for_dir(self) -> None:
        # if directory DNE, make one
        if not os.path.isdir(self.path_dloaded_vids):
            os.mkdir(self.path_dloaded_vids)


if __name__ == "__main__":
    from TikTokApi import TikTokApi

    verifyFp = "verify_kxi0g713_fTOHLX63_ZzzR_4SPu_Alxi_Qvaiyt0sic7U"
    api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
    vid_dicts = api.by_hashtag(hashtag="fyp", count=3)
    Downloader(api).download_all(vid_dicts)
