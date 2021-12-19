# A Tiktok to Youtube Pipeline Project
>Yurii this project is using python 3.10.0 btw

>if you are in favor please autoformat with Black

### How it works:

- Selenium webdriver opens tiktok.com in firefox(could also be modified to run in chrome)
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

- [ ] Perhaps Find a better way to manage our enviroments beyond just a requirements.txt file
- [ ] Implement getting desired video urls from tiktok.com
- [ ] Implement entering urls to Snaptik and downloading videos
- [ ] connecting video concat to run after tiktok scrapper
