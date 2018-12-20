import cv2
import numpy as np

img = cv2.imread('IMG_5634.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(gray,kernel,iterations = 2)
kernel = np.ones((4,4),np.uint8)
dilation = cv2.dilate(erosion,kernel,iterations = 2)

edged = cv2.Canny(dilation, 30, 200)

_, contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

rects = [cv2.boundingRect(cnt) for cnt in contours]
rects = sorted(rects,key=lambda  x:x[1],reverse=True)


i = -1
j = 1
y_old = 5000
x_old = 5000
for rect in rects:
    x,y,w,h = rect
    area = w * h

    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow("shapes", img)
cv2.imwrite("ee.jpg", img)
# cv2.imshow("Threshold", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()