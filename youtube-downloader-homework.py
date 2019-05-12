import pytube
import os
import subprocess

cUrl = input("YouTube 에서 동영상 주소를 복사해서 붙여넣어주세요: ")

if (cUrl != "") :
    yt=pytube.YouTube(cUrl)
    videos=yt.streams.all()


#print('videos', videos)

    for i in range(len(videos)) :
        print(i, ', ' ,videos[i])

cNum = int(input("다운받을 화질은?(0~21)"))

down_dir = "D:/Atom WorkSpace/Youtube"
videos[cNum].download(down_dir)
oriFileName = videos[cNum].default_filename
print("다운로드가 완료되었습니다.")

cConvert = input("MP3 파일로 음원을 추출합니까(Y/N): ")

if (cConvert=='y' or cConvert=="Y") :

    newFileName = input("Mp3 파일명:")


    subprocess.call(['ffmpeg','-i',os.path.join(down_dir,oriFileName), os.path.join(down_dir,newFileName)+'.mp3'])

    print("MP3 변환 완료!")

else :
    print("mp3 변환을 진행하지 않습니다.")
