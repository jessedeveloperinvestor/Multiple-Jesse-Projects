#pip install moviepy
import moviepy.editor
video=moviepy.editor.VideoFileClip('path/video.mp4')
audio_video=video.audio
audio_video.write_audiofile('path/audio.mp3')