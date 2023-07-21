# Download Video from youtube using pytube

from pytube import YouTube

# Prompt user to input the YouTube video link
link = input(" Please Provide your Link : ")

# Create a YouTube object with the provided link
youtube_1 = YouTube(link)

# The available video streams to all videoes 
# videos = youtube_1.streams.all()

# Filter the available video streams to only include progressive streams
videos = youtube_1.streams.filter(progressive=True)

# Enumerate the progressive streams and print them with their corresponding indices
vid = list(enumerate(videos))
for i in vid:
    print(i)

# Prompt user to choose the index of the video they want to download
strm = int(input("Please provide the index you want to download : "))

# Download the selected video
videos[strm].download()

print("successfully downloaded")



