# A Tiktok to Youtube Pipeline Project
>Yurii this project is using python 3.10.0 btw

>if you are in favor please autoformat with
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### How it works:
- run tiktotube.sh script
- use unofficial tiktok api to get urls of desired videos: https://blog.devgenius.io/tiktok-api-python-41d76c67a833
- Grab the urls of the desired videos
- use the api to download the videos from their download urls
- Run video_editor.py script to concatenate all videos
- Boom!!, final video
- ...
- profit!!

---

### TODO:

- [x] figure out why the final video doesn't seem to have sound
- [ ] find a better way to general the os and path calls so it works on both of our operating systems. we could use docker if we feel extra lol
- [ ] should add comments to tiktok_api.py
- [x] make a "main.py" or something to run both scripts from

---

### Stretch Goals:
- youtube api that allows auto upload?
- better control over which kind of videos get downloaded from tiktok.(different catagories etc)

---
### setting up tikok Api
https://github.com/davidteather/tiktok-api
