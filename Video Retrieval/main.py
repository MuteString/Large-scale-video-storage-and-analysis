# coding:utf-8

import cv2 as cv
import numpy as np
from GetFeatures import get_features
import os
import pickle


def get_video_features(path, step):
    """
    获取样例视频的特征图序列
    :param path: 视频文件路径
    :param step: 提取帧的间隔
    :return: 视频特征序列
    """
    step_counter = 0
    Step = step   # 每间隔step帧提取一帧
    VideoName = path.split('\\')[-1].split('.')[0]
    VideoFeature = []
    Sample_Video = cv.VideoCapture(path)
    FPS = Sample_Video.get(cv.CAP_PROP_FPS)
    while Sample_Video.isOpened():
        ret, Sample_Frame = Sample_Video.read()
        if not ret:
            break
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        if step_counter % step == 0:
            frame_feature = get_features(Sample_Frame)
            VideoFeature.append(frame_feature)
        step_counter += 1
    Sample_Video.release()
    return VideoFeature, FPS


def video_similarity(samples, video, step):
    """
    计算两个视频时间的相似度
    :param samples: 样例视频的特征图序列
    :param video: 待检索视频的特征图序列
    :return: min_dist:待检索视频和样例视频的距离
             min_start_time:最相似的帧序列在视频中的开始时间
    """
    length_sample = len(samples[0])
    length_video = len(video[0])
    min_dist = 9999999999999
    min_start_frame = 0
    if length_sample <= length_video:
        for wind_i in range(0, int(length_video/length_sample)):
            dist = 0
            for j in range(length_sample):
                # dist += np.linalg.norm(np.array(samples[wind_i*length_sample+j])
                # - np.array(video[wind_i*length_sample+j]))
                dist = np.sqrt(np.sum(np.square(
                    np.array(samples[0][j]) - np.array(video[0][wind_i*length_sample+j]))))
            if dist <= min_dist:
                min_dist = dist
                min_start_frame = wind_i * length_sample
    else:
        for wind_i in range(0, int(length_sample/length_video)):
            dist = 0
            for j in range(length_video):
                # dist += np.linalg.norm(np.array(samples[wind_i*length_video+j])
                # - np.array(video[wind_i*length_video+j]))
                dist = np.sqrt(np.sum(np.square(
                    np.array(samples[0][wind_i * video + j]) - np.array(video[0][j]))))
            if dist <= min_dist:
                min_dist = dist
                min_start_frame = wind_i * length_video
    min_start_time = float(min_start_frame * step / video[1])
    return min_dist, min_start_time


def get_file_path(file_dir):
    """
    遍历file_dir文件夹，获取待检索视频文件夹下的所有视频
    :param file_dir: 待检索视频所在路径
    :return:
    """
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.avi':
                L.append(os.path.join(root, file))
    return L


def get_all_video_feature(file_path, step):
    Step = step
    Video_Features_all = {}                # 用于存储所有待检测视频的特征序列
    Video_list = get_file_path(file_path)  # 获取所有待检测视频文件路径
    # 计算所有待检索视频的特征图序列
    for video in Video_list:
        Video_Features_all[video.split('\\')[2]] = get_video_features(video, Step)
        print("Get", video.split('\\')[2], 'feature map.')
    # 存储特征图序列
    trained_Feature = open('..\\trained_feature.pkl', 'wb')
    pickle.dump(Video_Features_all, trained_Feature)
    trained_Feature.close()


if __name__ == '__main__':
    # 初始化相关变量
    Step = 20                 # 选择帧的间隔
    Dist_list = {}            # 存储所有待检测视频和样例视频的距离（距离越小相似度越高）

    # 获取所有待检索视频的特征图序列(只需执行一次)
    get_all_video_feature('..\\Videos4Retrieval', 20)

    # 获取样例视频特征图序列
    Sample_Path = "SampleVideo\\v_biking_01_02.avi"
    Sample_Feature = get_video_features(Sample_Path, Step)
    print('Get Sample Video feature map.')

    # 加载事先存储的所有视频的特征图序列
    trained_feature = open('..\\trained_feature.pkl', 'rb')
    Video_Features_ALL = pickle.load(trained_feature)

    # 进行特征匹配
    for video in Video_Features_ALL:
        Dist_list[video] = video_similarity(Sample_Feature, Video_Features_ALL[video], Step)
        print("Get", video, 'distance.')
    sorted_Dist = sorted(Dist_list.keys())
    print(r"######## Similar Video ##########")
    for i in sorted_Dist:
        print(i)
