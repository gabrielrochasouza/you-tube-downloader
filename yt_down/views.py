import os
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
        import webbrowser
        webbrowser.open(video_url, new=1)
        return render(request, "downloaded-file.html")
    except Exception:
        return render(request, "error.html")
    

        
 
def download_video(request):
    url = request.GET.get("url")
    try:
        yt = pytube.YouTube(url)
        streams = []
        for stream in yt.streams.filter(progressive=True):
            streams.append(stream)
    except Exception:
        return render(request, "error.html")

    return render(request, 'download.html',{"url":url, "streams":streams, "title": yt.title, "thumbnail":yt.thumbnail_url, "description":yt.description})
