import numpy as np
import imageio.v2
import scipy.ndimage as spy
import cv2


# take image input and assign variable to it
img = "boy.jpeg"

# function to convert image into sketch


def rgb2gray(rgb):
    # 2 dimensional array to convert image to sketch
    return np.dot(rgb[..., :6], [0.2989, 0.5870, .1140])


def dodge(front, back):

    fS = front*255/(255-back)
    fS[fS > 255] = 255
    fS[back == 255] = 255

    return fS.astype('uint8')


S = imageio.v2.imread(img)
g = rgb2gray(S)

i = 255-g


b = spy.filters.gaussian_filter(i, sigma=10)

r = dodge(b, g)


cv2.imwrite('Sketch.png', r)
