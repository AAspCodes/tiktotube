# A Tiktok to Youtube Pipeline Project
>Yurii this project is using python 3.10.0 btw

>if you are in favor please autoformat with Black

### How it works:

- selenium webdriver opens tiktok.com in firefox
- grabs the urls of the desired videos
- selenium webdriver opens https://snaptik.app/en (snaptik, is a site for downloading tiktok videos)
- for each video:
    - enter tiktok video url into snap tik, and click download
    - download the video


- run video_editor.py script to concatenate all videos

- boom, final video...



------------------------------------------------------------------------------------------
### Stretch Goals:
- youtube api that allows auto upload?
- better control over which kind of videos get downloaded from tiktok.(different catagories etc)


---
### TODO:
- The main challenge of this project implementing tiktok_scrapper.py and the use of selenium.

- [ ] a better way to manage our enviroments beyond a requirements.txt file


---
# major issues

### Option 1: Use a selenium webdriver to scrape tikok.
- The problem is thought that tiktok is very defensive. Obviously they don't want us to rip off thier content. This makes my original approach of using a selenium webdriver troublesome, as it immediately does "are you robot" checks. It stops you so much and makes you pull out your phone. And it seems to intentionally act different each time.

### Option 2:
- https://tikapi.io/
- https://github.com/davidteather/TikTok-Api
- There is an unofficial tiktok API. Its paid ($27 per month at a minimum) but has a free 5 day trial. Is it it worth it for us to use the trial just to make get through the development and then never run the project again after five days? Could we string together multiple free trials?

### Option 3:
- TikTok has an official API, but its has tough approval, and is meant only for proffesionals that are serious about integrateing tiktok into thier projects.


### Option 4:
- Continue the project, but not with tiktok lol, scrape something else? idk
