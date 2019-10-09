import time,os
import glob

FFMPEG_PATH = 'E:/ffmpeg/ffmpeg-20190826-0821bc4-win64-static/bin/ffmpeg.exe'
VIDEO_DIR  = 'd:\\'

def recording():
    #输出视频文件
    outputfile = VIDEO_DIR + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.mp4'

    #执行语句
    setting = '-y -rtbufsize 100M -f gdigrab -framerate 10' \
              ' -draw_mouse 1 -i desktop-c:v libx264 -r 20' \
              ' -crf 35 -pix_fmt yuv420p ' \
              '-fs 100M "%s"'% outputfile        #其中 %s 部分 是需要填入 产生的视频文件名。
    recordingCmdLine = FFMPEG_PATH + ' ' + setting
    # 查看命令内容
    print(recordingCmdLine)

    # 执行命令录制视频
    os.system(recordingCmdLine)

def merging():
    #合并视频
    os.chdir(VIDEO_DIR)     #os.chdir() 方法用于改变当前工作目录到指定的路径。
    fileList = glob.glob(VIDEO_DIR + '*.mp4')    #返回所有匹配的文件路径列表
    fileList = [os.path.basename(one) for one in fileList]     # # 查询路径中包含的文件名

    if fileList:
        print('\n目录中没有这些视频文件')
    else:
        print('\n目录中没有视频文件')
        return

    idx = 1
    for one in fileList:
        print('%s - %s'%(idx,one))
        idx += 1

    print('\n请选择要合并视频的视频文件序号(格式 1,2,3,4) :', end=' ')

    mergeSequence = input('')
    videoFilesToMer = mergeSequence.split(',')
    videoFileNamesToMer = [fileList[int(one.strip()) - 1] for one in videoFilesToMer]
