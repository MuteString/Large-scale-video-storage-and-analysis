# coding: utf-8

import numpy as np
import math
import cv2 as cv

PI = math.pi


def F(r, v, image_height, image_width, image):
    x = int(r*math.cos(PI*v/180)+image_height/2)
    y = int(r*math.sin(PI*v/180)+image_width/2)
    f = float(image[x][y])/255
    return f


def B(v, q, r, image_height, image_width, image):
    b1 = F(r, 0, image_height, image_width, image)
    b2 = F(r, 1, image_height, image_width, image)

    for i in range(2, 359):
        b1 = F(r,v,image_height, image_width, image)+b2*2*math.cos(q)-b1
        temp = b1
        b1 = b2
        b2 = temp
    return b1, b2


def T(p, r, N):
    if p == 0:
        t = 1
    elif p == 1:
        t = (2*r+1-N)/N
    else:
        t = ((2*p-1)*(2*r+1-N)/N*T(p-1, r, N)-(p-1)*T(p-2, r, N)*(N**p-(p-1)**2))/p/N**p
    return t


def fast_tchebichef(p, q, image_height, image_width, image):
    """
    化简后的Tchebichef矩计算
    :param p:
    :param q:
    :param image_height: 灰度图像的高
    :param image_width: 灰度图像的宽
    :param image: 灰度图像
    :return:
    """
    m = min(int(image_height/2-1), int(image_width/2-1))
    sum = 0
    I = math.cos(q*358*PI/180)
    K = math.cos(q*359*PI/180)
    for i in range(m):
        b1, b2 = B(358, q, i, image_height, image_width, image)
        sum = sum+(b2*I+F(i, 359, image_height, image_width, image)*K
                   - F(i, 0, image_height, image_width, image)-b1*K)*T(p, i, image_width)
    S = sum/360
    return S


def tchebichef_features(image):
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image_height = image.shape[0]
    image_width = image.shape[1]
    t_feature = np.zeros(5)
    for i in range(5):
        t_feature[i] = (fast_tchebichef(i, 8, image_height, image_width, image) + 1) / 2
    return t_feature


if __name__ == '__main__':
    image = cv.imread('v_shooting_01_01_0.jpg')
    t_feature = tchebichef_features(image)
    print(t_feature)
