from pytube import YouTube
link = "https://www.youtube.com/watch?v=LqYIKYEnX7Y"
yt = YouTube(link)
title = yt.title
print(title)
t=yt.streams.filter(only_audio=True).all()
t[0].download('C:/temp')
