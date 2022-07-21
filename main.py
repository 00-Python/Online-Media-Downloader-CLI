import os
from datetime import date, datetime, time

import instaloader
from instaloader import Profile
from instaloader.structures import Post
from pytube import YouTube

# function for downloading music or videos from youtube
def yt_download():
    selection = str.lower(input('Would you like to download a video or music? (v/m): '))
    try:
        if selection == 'video' or selection == 'v':
            link = input('Enter video url: ')
            video = YouTube(link)
            stream = video.streams.get_highest_resolution()
            stream.download('Videos/')
            print('Finished')
        elif selection == 'music' or selection == 'm':
            file_path = os.getcwd()
            link = input('Enter song url: ')
            video = YouTube(link)
            stream = video.streams.get_audio_only()
            stream.download(file_path + '\\Music\\')
            mp4_vid_title = str(video.title)
            mp4_vid_title_path = file_path+'\\Music\\'+mp4_vid_title+'.mp4'
            mp3_title_path = file_path+'\\Music\\'+mp4_vid_title+'.mp3'
            mp4_vid_title_path = mp4_vid_title_path.replace('\\', '/')
            mp3_title_path = mp3_title_path.replace('\\', '/')
            os.rename(mp4_vid_title_path, mp3_title_path)
            print('Finished')
        else:
            print('Incorrect selection!!')
    except:
        print('Error, Try again!')

# function for downloading images or videos from instagram
def ig_downloader():
    #get instance
    L = instaloader.Instaloader()
    # details
    selection = str.lower(input('What do you want to download? (Whole profile: profile, single image: image, single video: video or profile pic: pp): '))
    try:
        if selection == 'profile':
            uname = input('Enter username of the profile you would like to download: ')
            L.download_profile(uname)
            print('Done')
        elif selection == 'image':
            url = input('Enter the url of the image you want to download: ')
            time = str(datetime.now())
            file = str(r'img_'+time)
            L.download_pic(url=url, mtime=time, filename=file)
            print('Done')
    except:
        print('Error, Try again! ')
        exit

dw_source = str.lower(input('Where would you like to download from (Youtube: yt / Instagram: ig)? '))
if dw_source == 'yt' or dw_source == 'youtube':
    yt_download()
elif dw_source == 'ig' or dw_source == 'instagram':
    ig_downloader()
else:
    print('Not supported yet')
