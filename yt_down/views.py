from django.shortcuts import render
import pytube

# Create your views here.

def main_page(request):
    return render(request,"main.html")


def download_video_page(request):
    return render(request, "video-downloader.html")


def download_mp3_page(request):
    return render(request, "mp3-downloader.html")


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
