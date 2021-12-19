# A Tiktok to Youtube Pipeline Project
>Yurii this project is using python 3.10.0 btw

>if you are in favor please autoformat with Black

### How it works:

- unofficial tiktok api to get urls of desired videos: https://blog.devgenius.io/tiktok-api-python-41d76c67a833
- Grab the urls of the desired videos
- Selenium webdriver opens https://snaptik.app/en (snaptik, is a site for downloading tiktok videos)
- For each video:
    - Enter tiktok video url into snap tik, and click download
    - Download the video


- Run video_editor.py script to concatenate all videos

- Boom!!, final video
- ...
- profit!!



------------------------------------------------------------------------------------------
### Stretch Goals:
- youtube api that allows auto upload?
- better control over which kind of videos get downloaded from tiktok.(different catagories etc)


---
### TODO:
- The main challenge of this project implementing tiktok_scrapper.py and the use of selenium.

- [ ] a better way to manage our enviroments beyond a requirements.txt file
- [ ] figure out why the final video doesn't seem to have sound
- [ ] find a better way to general the os and path calls so it works on both of our operating systems. we could use docker if we feel extra lol


---


### setting up tikok Api
https://github.com/davidteather/tiktok-api

also he kinda already did what we are doing ...
