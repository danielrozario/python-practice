from pytube import YouTube
link = "https://www.youtube.com/watch?v=EAYlckSaviI&t=73s"
yt = YouTube(link)
print(yt.title)
print(yt.thumbnail_url)
yt.streams.filter(only_audio=True)

