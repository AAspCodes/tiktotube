import json
import os

from rich.traceback import install as ad_fancy_traceback
from TikTokApi import TikTokApi

ad_fancy_traceback()


## you will likely need to replace this with your own see article : https://blog.devgenius.io/tiktok-api-python-41d76c67a833
verifyFp = "verify_kxdoktdi_4f9WkyIC_IlKW_4ucX_89jY_j3EaD4Z4uA80"


def get_video_dicts():
    api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
    return api, api.by_trending(count=2)


def log_video_dicts(video_dicts, path="api_output.json"):
    with open("api_output.json", "w") as f:
        f.write(json.dumps(video_dicts))


def get_download_url(video_dict):
    return video_dict["video"]["downloadAddr"]


def filter_download_urls(video_dicts):
    return [get_download_url(video_dict) for video_dict in video_dicts]


def download_videos(api, urls,save_path='./downloaded_videos/'):
    if not os.path.isdir(save_path):
        os.mkdir(save_path)
    for index, download_url in enumerate(urls):
        video_bytes = api.get_video_by_download_url(download_url)
        # Create a save dir if there is not one
        with open(os.path.join(save_path,f"saved_video{index}.mp4"), "wb") as f:
            f.write(video_bytes)


if __name__ == "__main__":
    api, video_dicts = get_video_dicts()
    # log_video_dicts(video_dicts)
    urls = filter_download_urls(video_dicts)
    download_videos(api, urls)
