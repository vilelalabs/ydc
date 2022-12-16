from pytube import YouTube
import os
import glob
from moviepy.editor import *

# --- get url from user
full_url = input('Enter the url of the video you want to download: ')
short_url =  full_url.replace('https://www.youtube.com/watch?v=', 'https://youtu.be/')

# --- download video from youtube
print('Downloading video. This process may take a while...')
YouTube(short_url).streams.first().download()
yt = YouTube(full_url)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

# --- delete .3gpp files
for i, filename in enumerate(glob.glob('*.3gpp')):
    os.remove(filename)

# --- change name of  all .mp4 file to music{n}.mp4
for i, filename in enumerate(glob.glob('*.mp4')):
    os.rename(filename, 'music{}.mp4'.format(i+1))


# --- convert all videos(mp4) to mp3
print('Converting all videos to mp3. This process may take a while...')
for i, filename in enumerate(glob.glob('*.mp4')):
    clip = VideoFileClip(filename)
    # write with same name but .mp3 extension
    clip.audio.write_audiofile('{}.mp3'.format(filename[:-4]))

# -- delete mp4 files
for i, filename in enumerate(glob.glob('*.mp4')):
    os.remove(filename)


# example video >> https://youtu.be/rUWxSEwctFU