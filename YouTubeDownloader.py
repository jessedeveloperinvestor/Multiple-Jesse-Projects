from pytube import YouTube
while True:
	print('Hi there, please type the link of the video to be downloaded and hit enter')
	link=input()
	video=YouTube(link)
	stream=video.streams.get_highest_resolution()
	stream.download(output_path='videos')
	print("\nThe download is complete, type 'exit' and hit enter to leave")
	if link == 'exit':
		break
