import os
import subprocess

files = os.listdir("vidoes")

for file in files:
    video_no = file.split("rse-")[1].split(".")[0]
    print(video_no)
    vid_name = file.split(".")[1].split("-in")[0]
    print(vid_name)

    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{video_no}-{vid_name}.mp3"])