from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=Jdxr2hTj2cY"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)
version = yt.streams.filter(res='720p')
audio = yt.streams.filter(only_audio=True)
print(version)
print(audio)
# stream = yt.streams.get_by_itag(398)
# stream.download()
A_down = yt.streams.get_by_itag(139)
A_down.download()
