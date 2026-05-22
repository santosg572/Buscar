import yt_dlp

#url = "https://youtu.be/UWKQca26LLo?si=BFA1ctYWY5grbKFN"
#url = "https://youtu.be/VZlKRYcHNoQ?si=VE98LLOpBBivofR-"
url = "https://youtu.be/Lr1TQpP3OZU?si=VRZ0QWKcyLnPgxvs"

ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])



