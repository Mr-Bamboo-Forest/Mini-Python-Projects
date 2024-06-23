from pytube import YouTube, Playlist
from moviepy.editor import VideoFileClip
from sys import argv
import os

# Check if the required number of arguments are provided
if len(argv) < 3:
    print("Usage: py ytDownloader.py <link> <usertype>")
    print("<usertype> should be one of: video (or v), playlist (or p), audiovideo (or av), audioplaylist (or ap)")
    exit(1)

link = argv[1]
usertype = argv[2]
pytype = "nothing rn bro"

if usertype == "video" or usertype == "v":
    pytype = "mp4"
elif usertype == "playlist" or usertype == "p":
    pytype = "playlist"
elif usertype == "audiovideo" or usertype == "av":
    pytype = "mp3"
elif usertype == "audioplaylist" or usertype == "ap":
    pytype = "mp3playlist"
else:
    print(f"Invalid usertype: {usertype} should be one of: video (or v), playlist (or p), audiovideo (or av), audioplaylist (or ap)")
    exit(1)

download_path = r'C:\Users\Downloads'  # Change this to your desired directory

# Ensure the download path exists
if not os.path.exists(download_path):
    try:
        os.makedirs(download_path)
    except PermissionError as e:
        print(f"Error: {e}")
        print(f"Permission denied to create directory: {download_path}")
        exit(1)

if pytype == "playlist":
    p = Playlist(link)
    print("Playlist Title: ", p.title)
    videodownloaded = 0
    for video in p.videos:
        video.streams.first().download(download_path)
        videodownloaded += 1
        if videodownloaded == 1:
            print(videodownloaded, " video has been downloaded.")
        else: 
            print(videodownloaded, " videos have been downloaded.")
                  
elif pytype == "mp4":
    yt = YouTube(link)
    print("Title: ", yt.title)
    yd = yt.streams.get_highest_resolution()
    yd.download(download_path)
    print("Done Downloading, ", yt.title)

elif pytype == "mp3":
    m = YouTube(link)
    print("Title: ", m.title)
    mv = m.streams.filter(only_audio=True).first()
    out_file = mv.download(download_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print("Done Downloading, ", m.title, " as a .mp3 file")

elif pytype == "mp3playlist":
    pv = Playlist(link)
    print("Playlist Title: ", pv.title)
    videodownloaded = 0
    for video in pv.videos:
        out_file = video.streams.first().download(download_path)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        video_clip = VideoFileClip(out_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(new_file)
        audio_clip.close()
        video_clip.close()
        os.remove(out_file)
        videodownloaded += 1
        if videodownloaded == 1:
            print(videodownloaded, " video has been downloaded and converted to MP3.")
        else: 
            print(videodownloaded, " videos have been downloaded and converted to MP3.")

else: 
    print("womp womp womp")



#to use, ensure that vsc is being used: pytube, moviepy and venv are downloaded and use this in the terminal ctrl+shift+` 
#video
    #py ytDownloader.py "https://www.youtube.com/(link)" video
    #py ytDownloader.py "https://www.youtube.com/(link)" v
#playlist
    #py ytDownloader.py "https://www.youtube.com/(link)" playlist 
    #py ytDownloader.py "https://www.youtube.com/(link)" p
#audio mp3 (one file)
    #py ytDownloader.py "https://www.youtube.com/(link)" audiovideo
    #py ytDownloader.py "https://www.youtube.com/(link)" av
#audio mp3 playlist
    #py ytDownloader.py "https://www.youtube.com/(link)" audioplaylist
    #py ytDownloader.py "https://www.youtube.com/(link)" ap
    