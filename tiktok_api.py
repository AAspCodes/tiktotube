import json
import os
from typing import Dict, List
import re

from rich.traceback import install as ad_fancy_traceback
from TikTokApi import TikTokApi
from downloader import Downloader

ad_fancy_traceback()


class Tiktube:
    '''Allows to download videos from TikTok basing on hashtags.'''
    def __init__(self,verifyFp, min_view_count: int, min_video_count: int) -> None:
        '''Arguments:
        
           min_video_count - minimum number of tiktoks with a hashtag.
           min_view_count - minimum number of total number of views of all tiktoks with a hashtag.'''

        # Used to interact with TikTok
        self.api = TikTokApi.get_instance(custom_verifyFp=verifyFp)
        # Invalid hashtags are needed for filtering
        with open('invalid_hashtags.json') as json_file:
            self.invalid_hashtags = set(json.load(json_file)["hashtags"])
        # Ids and tags of tiktoks that have already been used in compilations
        with open('used_tiktoks.json') as json_file:
            self.used_tiktoks = json.load(json_file)
        # Used to calculate whether a hashtag is popular
        self.min_view_count = min_view_count
        self.min_video_count = min_video_count


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
        # TODO narrow the exception, the exceptions in the TikTokApi docs do not work.
        except Exception:
            # If tiktoks with the specified hashtags were not found, send a dict with stats that contain 0s.
            return {'videoCount': 0, 'viewCount': 0}

        

    def is_hashtag_popular(self, hashtag: str) -> bool:
        '''Returns a boolean which indicates whether the passed hashtag is popular.
                        
           Arguments:

           hashtag - hashtag to check whether it is popular.'''
        hashtag_stats = self.get_tiktok_stats_by_hashtag(hashtag)
        return hashtag_stats['videoCount']>=self.min_video_count and hashtag_stats['viewCount']>=self.min_view_count

    def get_tiktoks_by_tags(self, hashtags: List, max_compilation_duration_seconds: int) -> List:
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
                # TODO Fix this. I am not sure why, but it throws an exception that tag does not exist 
                # although it passed the popularity test, and if you run the function again it find videos with this tag.
                while True:
                    try:
                        video = self.api.by_hashtag(hashtag[1:],count=1,offset=offset)[0]
                        break
                    except Exception:
                        continue 

                # If video has already been used in a compilation, skip it
                if video['id'] not in self.used_tiktoks:
                    # Save used tiktok in format tiktok_id:tiktok_tags
                    self.used_tiktoks[video['id']] = self.get_hashtags(video['desc'])
                    # Add tiktok to video_list which will be returned
                    videos_list.append(video)
                    # Update the length of the compilation
                    total_duration_seconds+=video['video']['duration']
                    # Increment offset to fetch a new tiktok next iteration
                    offset+=1

        return videos_list

    
    def get_trending_hashtags(self) -> List:
        '''Searches for hashtags in trending tiktoks.
            
            Returns a list with trending tiktoks, or an empty string if there is no appropriate hashtags in first 500 trending videos.'''
        # Get 100 trending tiktoks
        videos = self.get_trending_tiktoks(100)
        for video in videos:
            video_description = video['desc']
            video_hashtags = self.get_hashtags(video_description)
            filtered_hashtags = []
            # if the description contains at least one tag
            if video_hashtags:
                for hashtag in video_hashtags:
                    if self.is_hashtag_valid(hashtag) and self.is_hashtag_popular(hashtag):
                        filtered_hashtags.append(hashtag)
                # If there is at least one hashtag left after filtering
                if filtered_hashtags:
                    return filtered_hashtags
        # If there is no tags in 100 trending videos, return an empty list
        return []


    
    def download_tiktoks(self, max_compilation_duration_seconds: int,
                            hashtags_list: List=[],
                            path_to_dloaded_vids: str="downloaded_videos",
                            video_prefix: str="saved_video" ) -> None:
        '''Download tiktoks basing on the passed hashtags to a specified directory.
            If no hashtags were passed, it looks for trending hashtags and downloads videos
            with max_compilation_duration_seconds basing on those tags.'''
        # TODO Edit description of function.
        # if the user did not pass any hashtags
        if not hashtags_list:
            # Find trending hashtags
            hashtags_list = self.get_trending_hashtags()

        
        # Class for tiktoks downloading
        # TODO change downloader code to create a subdir for hashtags
        # Subdir has to be names as hashtags, not video_prefix
        self.downloader = Downloader(self.api,path_to_dloaded_vids,video_prefix=''.join(hashtags_list))
        # Get tiktoks basing on hashtags
        video_dicts = self.get_tiktoks_by_tags(hashtags_list,max_compilation_duration_seconds)
        if video_dicts:
            # Download those tiktoks
            self.downloader.download_all(video_dicts)
            # Save updated used_tiktoks dict to a json file
            with open("used_tiktoks.json", "w") as outfile:
                json.dump(self.used_tiktoks, outfile)
        else:
            print('No TikToks were found with those tags.')
            




if __name__ == "__main__":
    #Has to be updated everytime to fetch new data from TikTok
    #TODO make the process of update automatic
    verifyFp = "verify_kxdoktdi_4f9WkyIC_IlKW_4ucX_89jY_j3EaD4Z4uA80"
    tiktube = Tiktube(verifyFp,min_video_count=2069,min_view_count=3800000)
    tiktube.download_tiktoks(max_compilation_duration_seconds=180)
   
