import os
import re
from typing import BinaryIO
from flask import send_file, redirect
from django.shortcuts import render
import pytube
from io import BytesIO

# Create your views here.

def main_page(request):
    return render(request,"main.html")

def download_video_page(request):
    return render(request, "video-downloader.html")

def download_mp3_page(request):
    return render(request, "mp3-downloader.html")

def video_downloaded(request):
    try: 
        request.POST.get("resolution")
        url = request.POST.get("url")
        buffer = BinaryIO()
        itag = request.POST.get("resolution")
        homedir = os.path.expanduser('~')
        dirs = homedir + "/Downloads"
        yt = pytube.YouTube(url)
        render(request, "downloaded-file.html")
        video = yt.streams.get_by_itag(itag)

        video_url = video.url
        video.stream_to_buffer(buffer)
        buffer.seek(1)
        print(video_url)
        import webbrowser
        webbrowser.open(video_url, new=1)

        # video.download(filename="video.mp4", output_path="video_files")
        # send_file("video_files/video.mp4", mimetype="video/mp4")
        return render(request, "downloaded-file.html")
    except Exception:
        return render(request, "error.html")
    

        
 
def download_video(request):
    url = request.GET.get("url")
    try:
        yt = pytube.YouTube(url)
        streams = []
        for stream in yt.streams.filter(progressive=True):
            stream.megabytes = round(stream.filesize/1000000,3)
            streams.append(stream)
            
    except Exception:
        return render(request, "error.html")

    return render(request, 'download.html',{"url":url ,"streams":streams, "title": yt.title, "thumbnail":yt.thumbnail_url, "description":yt.description})
