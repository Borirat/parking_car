import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
###########################

image = cv2.imread('a6.jpg',1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (21, 21), 0)
thresh = ~(cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1])
#cv2.imshow("test",thresh)
#ret1,thresh = cv2.threshold(thresh,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
sum_col = sum(thresh)
cv2.imshow("test",thresh)
for i in range(len(sum_col)):
    if sum_col[i] != 0 :
        break
print(i)
ini = i

sum_col_rev = sum_col[::-1]

for i in range(len(sum_col_rev)):
    if sum_col_rev[i] != 0 :
        break

fnl = len(sum_col_rev) - i
print(fnl)

sum_row = sum(cv2.transpose(thresh))

for i in range(len(sum_row)):
    if sum_row[i] != 0 :
        break
print(i)
ini_r = i

sum_row_rev = sum_row[::-1]

for i in range(len(sum_row_rev)):
    if sum_row_rev[i] != 0 :
         break

fnl_r = len(sum_row_rev) - i
print(fnl)

image = image[ini_r:fnl_r , ini:fnl]
cv2.imshow("Image", image)
cv2.imwrite('test.jpg',image)

###########################
all_sum = []

###########################
all_plate = []

for i in range(10):
    plate = ('province_crop%d.jpg'%(i))
    all_plate.append(plate)
print(all_plate)

for j in range(len(all_plate)):
    img = cv2.imread(all_plate[j],0)
##
    template = cv2.imread('test.jpg',0)
    w, h = template.shape[::-1]
    w1,h1 = img.shape[::-1]

    resized = cv2.resize(img, (w,h))
    ret1,img_1 = cv2.threshold(template,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    ret2,img_2 = cv2.threshold(resized,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
##cv2.imshow("img ", img_1)
##cv2.imshow("resized ", img_2)
    img_3 = abs(img_1-img_2)
##
##cv2.imshow("3", img_3)
##
##print(type(img_3))
    sum_img = sum(sum(img_3))
    all_sum.append(sum_img)

min_of_all = max(all_sum)
print("len = ",len(all_sum))
print("min = ",min_of_all)
for i in range(len(all_sum)):
    print("sum = ",all_sum[i])
    if(min_of_all==all_sum[i]):
        index = i
        break
print(index)
imageshow = cv2.imread(all_plate[index],0)
cv2.imshow("show",imageshow)
print(all_sum)
                  



























