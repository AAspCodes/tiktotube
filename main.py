import sys

import tiktok_api
import video_editor

if len(sys.argv) != 2:
    print('Should have 2 args, ["main.py", "<arg>"]')
    print(f"Instead found {len(sys.argv)} args = {sys.argv}")
    exit(0)

hashtag_source = sys.argv[1]
# This is intended simply as a place holder
# and should be modified to fit with how Yurri decideds to implement tiktok_api.py
if hashtag_source == "tiktok":
    print("running with tikok arg")
    # tiktok_api.tiktokrun()
    pass
elif hashtag_source == "google":
    print("running with google arg")
    # tiktok_apt.googlerun()
    pass
else:
    print('arg should have "tiktok" or "google", the shell script screwed up')
    pass

## temp until tiktok_api,py has interface built
tiktok_api.run()
video_editor.run()

exit(0)
