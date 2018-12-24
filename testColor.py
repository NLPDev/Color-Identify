#Crop image as polygen.


# import numpy
# from PIL import Image, ImageDraw
#
# # read image as RGB and add alpha (transparency)
# im = Image.open("crop.jpg").convert("RGBA")
#
# # convert to numpy (for convenience)
# imArray = numpy.asarray(im)
#
# # create mask
# polygon = [(444,203),(623,243),(691,177),(581,26),(482,42)]
# maskIm = Image.new('L', (imArray.shape[1], imArray.shape[0]), 0)
# ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
# mask = numpy.array(maskIm)
#
# # assemble new image (uint8: 0-255)
# newImArray = numpy.empty(imArray.shape,dtype='uint8')
#
# # colors (three first columns, RGB)
# newImArray[:,:,:3] = imArray[:,:,:3]
#
# # transparency (4th column)
# newImArray[:,:,3] = mask*255
#
# # back to Image from numpy
# newIm = Image.fromarray(newImArray, "RGBA")
# newIm.save("out.png")


import cv2
from PIL import Image

import colorsys

import math

def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v

print(rgb2hsv(186, 193, 199))
from skimage import io

# img=io.imread("out02.png")[:, :, : -1]
#
# average=img.mean(axis=0).mean(axis=0)
#
# print(average)
#
# print("--------")

im=Image.open("out.png")

image = cv2.imread("out.png")

ww, hh=im.size

print([ww, hh])


# if image type is b g r, then b g r value will be displayed.
# if image is gray then color intensity will be displayed.

crop_img=image[int(hh/2):int(hh/2)+100, int(ww/2):int(ww/2)+100]
cv2.imshow("crop", crop_img)



color = crop_img[5, 5]
print(color)

print(colorsys.rgb_to_hsv(186, 193, 199))

cv2.waitKey(0)
im=cv2.imread("ex01.jpg")

cv2.line(im, (0, 0), (50, 50), (int(color[0]),int(color[1]),int(color[2])), 5)
cv2.imshow("af", im)
cv2.waitKey(0)