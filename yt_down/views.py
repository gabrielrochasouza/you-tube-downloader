from django.shortcuts import render
import pytube
import youtube_dl
import os

def main_page(request):
    return render(request,"main.html")

def download_video_page(request):
    return render(request, "video-downloader.html")

def download_mp3_page(request):
    try: 
        return render(request, "mp3-downloader.html")
    except Exception:
        return render(request, "error.html")


def mp3_ready_to_download(request):
    try: 
        url = request.GET.get("url")
        options = {
            "format": "bestaudio/best",
            "keepvideo": False,
            "outtmpl": "audio.mp3",
            "path":"/static/"
            
        }
        video_info = youtube_dl.YoutubeDL().extract_info(
            url = url, download=False
        )
        with youtube_dl.YoutubeDL(options) as ydl:
            video_info = ydl.extract_info(
                url=url, download=False
            )
            thumbnail = video_info['thumbnail']
            url_to_download = video_info['url']

        return render(request, "mp3-ready-to-download.html",{
            "title":video_info['title'], 
            "description": video_info["description"],
            "thumbnail":thumbnail,
            "url_to_download":url_to_download
        })
    except Exception:
        return render(request, "error.html")


def video_downloaded(request):
    try:
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

    return render(request, 'download.html',{"url":url ,"download_link":streams[0].url, "streams":streams, "title": yt.title, "thumbnail":yt.thumbnail_url, "description":yt.description})
