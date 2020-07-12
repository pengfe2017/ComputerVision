from pytube import YouTube

YouTube('https://www.youtube.com/watch?v=AnccC_1o-Gg&t=2s').streams.get_highest_resolution().download()
 
#yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')