# coding:utf-8
import math
import cv2 as cv
import numpy as np


def hsv_features(image_path):
    """
    获取图像的HSV颜色特征
    :param image_path: 需要处理的图像路径
    :return: 处理得到的颜色特征向量
    """
    # 读取图片并从RBG色彩空间转换到HSV色彩空间
    image = cv.imread(image_path)
    image_height = image.shape[0]
    image_width = image.shape[1]
    image = cv.cvtColor(image, cv.COLOR_BGR2HSV_FULL)
    image_H = np.array(image[:, :, 0])/255    # 色调（Hue）分量
    image_S = np.array(image[:, :, 1])/255    # 饱和度(Saturation)分量
    image_V = np.array(image[:, :, 2])/255    # 亮度（Value）分量

    # 分区域计算HSV直方图
    t_feature = np.zeros(81)     # 初始化特征向量为0向量

    # 计算4x4区域中的第1列区域
    for i in range(math.floor(image_height/4), math.floor(image_height*3/4)):
        for j in range(math.floor(image_width/4)):
            tmp_h = math.floor(image_H[i][j]/0.111112)
            tmp_s = math.floor(image_S[i][j]/0.333334)
            tmp_v = math.floor(image_V[i][j]/0.333334)
            d = tmp_h*9+tmp_s*3+tmp_v+1
            t_feature[d] = t_feature[d] + 1

    # 计算4x4区域中的第4列区域
    for i in range(math.floor(image_height/4), math.floor(image_height*3/4)):
        for j in range(math.floor(image_width*3/4), math.floor(image_width)):
            tmp_h = math.floor(image_H[i][j] / 0.111112)
            tmp_s = math.floor(image_S[i][j] / 0.333334)
            tmp_v = math.floor(image_V[i][j] / 0.333334)
            d = tmp_h * 9 + tmp_s * 3 + tmp_v + 1
            t_feature[d] = t_feature[d] + 1

    # 计算4x4区域中的第1行区域
    for i in range(math.floor(image_height/4)):
        for j in range(math.floor(image_width/4), math.floor(image_width*3/4)):
            tmp_h = math.floor(image_H[i][j] / 0.111112)
            tmp_s = math.floor(image_S[i][j] / 0.333334)
            tmp_v = math.floor(image_V[i][j] / 0.333334)
            d = tmp_h * 9 + tmp_s * 3 + tmp_v + 1
            t_feature[d] = t_feature[d] + 1

    # 计算4x4区域中的第4行区域
    for i in range(math.floor(image_height*3/4), math.floor(image_height)):
        for j in range(math.floor(image_width/4), math.floor(image_width*3/4)):
            tmp_h = math.floor(image_H[i][j] / 0.111112)
            tmp_s = math.floor(image_S[i][j] / 0.333334)
            tmp_v = math.floor(image_V[i][j] / 0.333334)
            d = tmp_h * 9 + tmp_s * 3 + tmp_v + 1
            t_feature[d] = t_feature[d] + 1

    # 计算4x4区域中的中间区域
    for i in range(math.floor(image_height * 3 / 4), math.floor(image_height)):
        for j in range(math.floor(image_width / 4), math.floor(image_width * 3 / 4)):
            tmp_h = math.floor(image_H[i][j] / 0.111112)
            tmp_s = math.floor(image_S[i][j] / 0.333334)
            tmp_v = math.floor(image_V[i][j] / 0.333334)
            d = tmp_h * 9 + tmp_s * 3 + tmp_v + 1
            t_feature[d] = t_feature[d] + 2

    return t_feature


# 测试脚本
if __name__ == "__main__":
    image_path = "v_shooting_01_01_0.jpg"
    cv.imshow('original', cv.imread(image_path))
    hsvFeature = hsv_features(image_path)
    print(hsvFeature)
