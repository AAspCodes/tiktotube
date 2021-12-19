import json

from rich.traceback import install as ad_fancy_traceback
from TikTokApi import TikTokApi

ad_fancy_traceback()


## you will likely need to replace this with your own see article : https://blog.devgenius.io/tiktok-api-python-41d76c67a833
verifyFp = "verify_kxcmt49v_Mh9GhNFs_4RiC_4yVp_B1l7_X6ChWQQ5Qn5q"


def get_video_dicts():
    api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
    return api, api.by_trending(count=2)


def log_video_dicts(video_dicts, path="api_output.json"):
    with open("api_output.json", "w") as f:
        f.write(json.dumps(video_dicts, indent=4))


def get_download_url(video_dict):
    return video_dict["video"]["downloadAddr"]


def filter_download_urls(video_dicts):
    return map(get_download_url, video_dicts)


def download_videos(api, urls):
    for index, download_url in enumerate(urls):
        video_bytes = api.get_video_by_download_url(download_url)
        with open(f"./downloaded_videos/saved_video{index}.mp4", "wb") as f:
            f.write(video_bytes)


if __name__ == "__main__":
    api, video_dicts = get_video_dicts()
    # log_video_dicts(video_dicts)
    urls = filter_download_urls(video_dicts)
    download_videos(api, urls)
