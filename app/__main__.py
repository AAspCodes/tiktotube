from app.tiktok_api import Tiktube
from app.video_editor import VideoEditor


verifyFp = "verify_kxp2oq0e_PHBKNvBm_lZJX_4UKD_9EOF_u1QZlx3lDvmP"
# tiktok_api
tiktube = Tiktube(verifyFp, 30_000, 30_000)
tiktube.download_tiktoks(max_compilation_duration_seconds=30)
# video_editor
VideoEditor().edit()

# youtube uploader
