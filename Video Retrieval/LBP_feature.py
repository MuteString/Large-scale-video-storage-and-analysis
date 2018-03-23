# -*- coding: utf-8 -*-

from skimage.feature import local_binary_pattern
import scipy.io
import cv2
import numpy as np

# Get Mapping from matlab
mapping = scipy.io.loadmat('mapping.mat')
mapping['table'] = np.array(mapping['mapping_table']).T
mapping['samples'] = int(mapping['mapping_samples'])
mapping['num'] = int(mapping['mapping_num'])


def apply_mapping(mat, mapping):
    """
    将LBP矩阵映射成特征向量
    :param mat: LBP矩阵
    :param mapping: 映射表
    :return: 映射后得到的特征向量
    """
    result = np.zeros([mat.shape[0], mat.shape[1]])
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            result[i][j] = mapping['table'][int(mat[i][j])]
    single_result = []
    for i in result:
        single_result.extend(i)
    result_dict = {k: single_result.count(k)/(mat.shape[0]*mat.shape[1]) for k in set(single_result)}
    return result_dict


def lbp_feature(r, n, image_path):
    # settings for LBP
    radius = r
    n_points = n

    image = cv2.imread(image_path)  # 读取图像
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 转换为灰度图显示
    lbp = local_binary_pattern(image, n_points, radius)  # 提取LBP特征
    lbp_vec = apply_mapping(lbp, mapping)                # 映射特征到特征向量
    return lbp_vec
