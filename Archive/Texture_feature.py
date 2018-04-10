# coding: utf-8

from skimage.feature import greycomatrix, greycoprops
import skimage.io as skio
import skimage.color as skcolor
import numpy as np


def glcm_feature(image_gray):
    image_gray = np.uint(np.floor(image_gray / 0.33333334))
    glcm = greycomatrix(image_gray, [1], [0], 3)
    glcm_feature = [int(greycoprops(glcm, 'contrast')),
                    int(greycoprops(glcm, 'dissimilarity')),
                    int(greycoprops(glcm, 'homogeneity')),
                    int(greycoprops(glcm, 'energy')),
                    int(greycoprops(glcm, 'ASM')),
                    int(greycoprops(glcm, 'correlation'))]
    return glcm_feature


if __name__ == '__main__':
    image = skio.imread('v_shooting_01_01_0.jpg')
    image_gray = np.array(skcolor.rgb2gray(image))
    print(glcm_feature(image_gray))
