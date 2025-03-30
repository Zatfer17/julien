from pytubefix     import Channel, YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/@boilerroom"
c = Channel(url)

print(f'Downloading videos by: {c.channel_name}')

for video in c.videos[:100]:
    if "| Boiler Room" in video.title:
        try:
            print(video.title)
            yt = YouTube(video.watch_url, on_progress_callback=on_progress)
            ys = yt.streams.get_audio_only()
            ys.download("/Users/matteoferrini/Music/Boiler Room")
        except:
            continue