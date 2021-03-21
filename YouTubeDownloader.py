from pytube import YouTube
print('Hi there, please type the link of the video to be downloaded and hit enter')
link=input()
video=YouTube(link)
stream=video.streams.get_highest_resolution()
stream.download(output_path='videos')