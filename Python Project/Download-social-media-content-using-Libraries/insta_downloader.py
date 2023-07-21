# Download Video from YouTube using Instaloader

import instaloader

# Prompt user to input the Instagram profile name
profile_name = input("Enter Insta Profile name : ")

# Display a message indicating that the media download is starting
print("Downloading Media...")

# Create an Instaloader object and download the media from the specified Instagram profile
# If profile_pic_only is set to False, it will download all media including photos and videos
instaloader.Instaloader().download_profile(profile_name, profile_pic_only=False)

# Display a message to indicate that the download has been completed
print("Download Completed")
