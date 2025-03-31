from pytubefix     import Channel, YouTube
from pytubefix.cli import on_progress
from pathlib       import Path


# Config
MUSIC_PATH    = Path.home() / "Music" / "Boiler Room"
URL           = "https://www.youtube.com/@boilerroom"
TITLE_FILTER  = "| Boiler Room"
LENGTH_FILTER = 2700
VIEWS_FILTER  = 1000000

def main():
    c = Channel(URL)

    print(f'Downloading videos by: {c.channel_name}')

    for video in c.videos:
        if (TITLE_FILTER in video.title) & (video.length >= LENGTH_FILTER) & (video.views >= VIEWS_FILTER):
            try:
                print(video.title)
                yt = YouTube(video.watch_url, on_progress_callback=on_progress)
                ys = yt.streams.get_audio_only()
                ys.download(MUSIC_PATH)
            except:
                continue

if __name__ == "__main__":
    main()
