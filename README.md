# A Tiktok to Youtube Pipeline Project
>Yurii this project is using python 3.10.0 btw

>if you are in favor please autoformat with Black

### How it works:

- selenium webdriver opens tiktok.com in firefox(could also be modified to run in chrome)
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
