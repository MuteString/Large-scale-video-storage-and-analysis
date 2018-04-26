# coding: utf-8

import math
import numpy as np


def cosVector(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    num = float(np.dot(vec1, vec2))
    denom = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    cos = num / denom  # 余弦值
    # sim = 0.5 + 0.5 * cos  # 归一化
    return abs(cos)


def euclideanDist(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    dist = np.sqrt(np.sum(np.square(vec1 - vec2)))
    return dist


def corrcoef(vec1, vec2):
    n = len(vec1)
    sum1 = sum(vec1)
    sum2 = sum(vec2)
    sumofxy = np.dot(np.array(vec1), np.array(vec2))
    sumofx2 = sum([pow(i, 2) for i in vec1])
    sumofy2 = sum([pow(j, 2) for j in vec2])
    num = sumofxy - (float(sum1)*float(sum2)/n)
    den = math.sqrt((sumofx2 - float(sum1 ** 2) / n) * (sumofy2 - float(sum2 ** 2) / n))
    return num / den

