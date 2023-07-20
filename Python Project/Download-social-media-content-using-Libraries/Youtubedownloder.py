# Download Video from youtube using pytube

from pytube import YouTube

link = input(" Please Provide your Link ")

youtube_1 =YouTube(link)

# videos = youtube_1.streams.all()

videos = youtube_1.streams.filter(progressive= True)

vid = list(enumerate(videos))

for i in vid:
    print(i)
strm = int(input("please provide your index you want to download"))

videos[strm].download()

print("successfully downloaded")