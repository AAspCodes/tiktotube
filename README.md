A Tiktok to Youtube Pipeline Project



How it works:

selenium webdriver opens tiktok.com in firefox
grabs the urls of the desired videos

selenium webdriver opens https://snaptik.app/en (snaptik, is a site for downloading tiktok videos)
for each video:
enter tiktok video url into snap tik, and click download
download the video


run video_editor.py script to concatenate all videos

boom, final video...


stretch goals:
youtube api that allows auto upload?
better control over which kind of videos get downloaded from tiktok.(different catagories etc)