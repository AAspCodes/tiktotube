import json
import os
from typing import List
import re

from rich.traceback import install as ad_fancy_traceback
from TikTokApi import TikTokApi

ad_fancy_traceback()


## you will likely need to replace this with your own see article : https://blog.devgenius.io/tiktok-api-python-41d76c67a833
verifyFp = "verify_kxdoktdi_4f9WkyIC_IlKW_4ucX_89jY_j3EaD4Z4uA80"


class Tiktube:
    '''Allows to download videos from TikTok basing on hashtags.'''
    def __init__(self,verifyFp) -> None:
        # Used to interact with TikTok
        self.api = TikTokApi.get_instance(custom_verifyFp=verifyFp)

    def get_tags(self, string: str) -> List:
        '''Searches for hashtags in the passed string.
           Returns list of found hashtags or an empty list if no hashtag was found.
        
           Arguments:

           string - string that is searched for hashtags.'''

        hashtag_pattern = r'#\S*'
        hashtag_list = re.findall(hashtag_pattern,string)
        total_hashtag_list = []
        # Check whether every element in the list contain only one hashtag
        for hashtag in hashtag_list:
            # If more than one hashtag
            if hashtag.count('#')!=1:
                for sub_hashtag in hashtag.split('#'):
                    # If hashtag is not an empty string
                    if sub_hashtag:
                        total_hashtag_list.append('#'+sub_hashtag)
            else:
                total_hashtag_list.append(hashtag)

        return total_hashtag_list

    def get_trending_tiktoks(self, count: int) -> List:
        '''Returns a list of dictionaries with found trending tiktoks.
           
           Arguments:

           Count - number of tiktoks to fetch. '''
        return self.api.by_trending(count=count)


'''
def get_video_dicts():
    api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
    return api, api.by_trending(count=2)


def log_video_dicts(video_dicts, path="api_output.json"):
    with open("api_output.json", "w") as f:
        f.write(json.dumps(video_dicts, indent=4))


def get_download_url(video_dict):
    return video_dict["video"]["downloadAddr"]


def get_tag(video_dict):
    return video_dict["video"]["downloadAddr"]

def filter_download_urls(video_dicts):
    return map(get_download_url, video_dicts)

def filter_tags(video_dicts):
    return [get_download_url(video_dict) for video_dict in video_dicts]


def download_videos(api, urls,save_path='downloaded_videos'):
    if not os.path.isdir(save_path):
        os.mkdir(save_path)
    for index, download_url in enumerate(urls):
        video_bytes = api.get_video_by_download_url(download_url)
        # Create a save dir if there is not one
        with open(os.path.join(save_path,f"saved_video{index}.mp4"), "wb") as f:
            f.write(video_bytes)
'''

if __name__ == "__main__":
    #Has to be updated everytime to fetch new data from TikTok
    #TODO make the process of update automatic
    verifyFp = "verify_kxdoktdi_4f9WkyIC_IlKW_4ucX_89jY_j3EaD4Z4uA80"
    tiktube = Tiktube(verifyFp)
    # Find 1000 tiktoks and save their hashtags in a json file.
    video_dict = tiktube.get_trending_tiktoks(1000)
    dict = {'hashtags':[]}
    for video in video_dict:
        hashtags_list = tiktube.get_tags(video['desc'])
        if hashtags_list:
            dict['hashtags'].extend(hashtags_list)

    dict['hashtags'] = list(set(dict['hashtags']))
    with open("hashtags.json", "w") as outfile:
        json.dump(dict, outfile)

    #api, video_dicts = get_video_dicts()
    #log_video_dicts(video_dicts)
    #urls = filter_download_urls(video_dicts)
    #download_videos(api, urls)
