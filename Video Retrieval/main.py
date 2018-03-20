# coding:utf-8

import cv2 as cv
import numpy as np


def get_features(path, step):
    """
    获取样例视频的特征图序列
    :param path:
    :param step:
    :return:
    """
    step_counter = 0
    Step = step   # extract 1 frame interval 5 frames
    VideoName = path.split('\\')[-1].split('.')[0]
    Sample_Video = cv.VideoCapture(path)
    while Sample_Video.isOpened():
        ret, Sample_Frame = Sample_Video.read()
        if not ret:
            break
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        if step_counter % step == 0:
            # cv.imshow('Sample_Frame', Sample_Frame)
            cv.imwrite('FrameSet\\' + VideoName + '_' + str(step_counter) + '.jpg', Sample_Frame)
        step_counter += 1
    Sample_Video.release()
    # cv.destroyAllWindows()


def calc_similarity(samples, video):
    length_sample = len(samples)
    length_video = len(video)
    if length_sample <= length_video:
        for i in range(0, length_video, length_sample):
            feature_similarity(samples[i], video[i])
    pass


def feature_similarity():
    pass


Sample_Path = "SampleVideo\\v_shooting_01_01.avi"
get_features(Sample_Path, 5)


