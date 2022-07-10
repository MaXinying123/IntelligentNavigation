import os
from posixpath import splitext
import cv2
dirname="D:/learn/智能船舶导航地图/videos_test"
list=os.listdir(dirname)


for cur_file in list:
    cap=cv2.VideoCapture(dirname+"/"+cur_file)
    stem,suffix=os.path.splitext(cur_file)
    while True:
        sucess,frame=cap.read()
        if sucess:
            lastframe=frame
        else:
            break

    # 给截取到的最后一帧命名并保存
    print(cur_file+'处理完成')
    cv2.imwrite("TestSet/" + stem + '.jpg', lastframe)
