import json
import os
from typing import Dict, List
import re

from rich.traceback import install as ad_fancy_traceback
from TikTokApi import TikTokApi

ad_fancy_traceback()


class Tiktube:
    '''Allows to download videos from TikTok basing on hashtags.'''
    def __init__(self,verifyFp, min_view_count: int, min_video_count: int) -> None:
        '''Arguments:
        
           min_video_count - minimum number of tiktoks with a hashtag.
           min_view_count - minimum number of total number of views of all tiktoks with a hashtag.'''

        # Used to interact with TikTok
        self.api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
        # Class for tiktoks downloading
        self.downloader = Downloader(self.api)
        # Invalid hashtags are needed for filtering
        with open('invalid_hashtags.json') as json_file:
            self.invalid_hashtags = set(json.load(json_file)["hashtags"])
        # Ids and tags of tiktoks that have already been used in compilations
        with open('used_tiktoks.json') as json_file:
            self.used_tiktoks = json.load(json_file)
        # Used to calculate whether a hashtag is popular
        self.min_view_count = min_view_count
        self.min_video_count = min_video_count

    def __del__(self) -> None:
        '''Desctuctor.'''
        # Save updated used_tiktoks dict to a json file
        with open("used_tiktoks.json", "w") as outfile:
            json.dump(self.used_tiktoks, outfile)

    def get_hashtags(self, string: str) -> List:
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

           count - number of tiktoks to fetch. '''
        return self.api.by_trending(count=count)

    def is_hashtag_valid(self, hashtag: str) -> bool:
        '''Returns a boolean value which indicates whether the passed hashtag valid or invalid.
        
           Arguments:

           hashtag - hashtag to check.'''

        return hashtag not in self.invalid_hashtags

    def get_tiktok_stats_by_hashtag(self, hashtag: str) -> Dict:
        '''Returns videoCount and viewCount for the passed hashtag.
        
           Arguments:

           hashtag - hashtag to get stats for.'''

        # [1:] removes first character from the hashtag, which has to be #
        try:
            hashtag_object = self.api.get_hashtag_object(hashtag[1:])
            return hashtag_object['challengeInfo']['stats']
        except TikTokApi.exceptions.GenericTikTokError:
            # If tiktoks with the specified hashtags were not found, send a dict with stats that contain 0s.
            return {'videoCount': 0, 'viewCount': 0}

        

    def is_hashtag_popular(self, hashtag: str) -> bool:
        '''Returns a boolean which indicates whether the passed hashtag is popular.
                        
           Arguments:

           hashtag - hashtag to check whether it is popular.'''
        hashtag_stats = self.get_tiktok_stats_by_hashtag(hashtag)
        return hashtag_stats['videoCount']>=self.min_video_count and hashtag_stats['viewCount']>=self.min_view_count

    def get_tiktoks_by_tags(self, hashtags: List, max_compilation_duration_seconds: int) -> Dict:
        '''
        Arguments:

        hashtags - list of hashtags that will be used to find tiktoks.
        max_compilation_duration_seconds - the maximum duration of a compilation of tiktoks in seconds.
        '''
        videos_list = []
        total_duration_seconds = 0
        offset = 0

        while total_duration_seconds < max_compilation_duration_seconds:
            # TODO consider adding multithreading
            for hashtag in hashtags:
                video = self.api.by_hashtag(hashtag,count=1,offset=offset)

                # If video has already been used in a compilation, skip it
                if video['id'] not in self.used_tiktoks:
                    # Save used tiktok in format tiktok_id:tiktok_tags
                    self.used_tiktoks[video[id]] = self.get_hashtags(video['desc'])
                    # Add tiktok to video_list which will be returned
                    videos_list.append(video)
                    # Update the length of the compilation
                    total_duration_seconds+=video['video']['duration']
                    # Increment offset to fetch a new tiktok next iteration
                    offset+=1







    


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
    tiktube = Tiktube(verifyFp,min_video_count=100,min_view_count=25000)
    # Find 1000 tiktoks and save their hashtags in a json file.
    video_dict = tiktube.get_trending_tiktoks(1000)
    dict = {'hashtags':[]}
    for video in video_dict:
        hashtags_list = tiktube.get_hashtags(video['desc'])
        if hashtags_list:
            dict['hashtags'].extend(hashtags_list)

    dict['hashtags'] = list(set(dict['hashtags']))
    with open("hashtags.json", "w") as outfile:
        json.dump(dict, outfile)

    #api, video_dicts = get_video_dicts()
    #log_video_dicts(video_dicts)
    #urls = filter_download_urls(video_dicts)
    #download_videos(api, urls)
