import pytube
import os
import subprocess

yt=pytube.YouTube("https://www.youtube.com/watch?v=HgzGwKwLmgM")
videos=yt.streams.all()

#print('videos', videos)

for i in range(len(videos)) :
    print(i, ', ' ,videos[i])

#cNum = int(input("다운받을 화질은?(0~21)"))


down_dir = "D:/Atom WorkSpace/Youtube"
videos[0].download(down_dir)

#newFileName = input("Mp3 파일명:")
#oriFileName = videos[cNum].default_filename

#subprocess.call(['ffmpeg','-i',os.path.join(down_dir,oriFileName), os.path.join(down_dir,newFileName)])

#print("동영상 다운로드 및 mp3 변환 완료!")
