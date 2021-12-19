import json

from rich.traceback import install as ad_fancy_traceback
from TikTokApi import TikTokApi

ad_fancy_traceback()

verifyFp = "verify_kxcmt49v_Mh9GhNFs_4RiC_4yVp_B1l7_X6ChWQQ5Qn5q"

api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
trending = api.by_trending(count=1)

# with open("api_output.json", "w") as f:
#     f.write(json.dumps(trending))
## parse json for download url
download_address = trending[0]["video"]["downloadAddr"]
## download video's bytes
result = api.get_video_by_download_url(download_url=download_address)
## writes bytes to file
with open("./downloaded_videos/saved_video.mp4", "wb") as f:
    f.write(result)
