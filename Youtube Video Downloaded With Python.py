import pytube
from pytube import YouTube

link = input("Please, Enter Your Youtube Video URL:")
link = str(link)
youtube = pytube.YouTube(link)
youtube.streams.first().download()

print("Video Has Been Downloaded", link)