from imutils import contours
from skimage import measure
import numpy as np
import argparse
import imutils
import cv2
import time

province = []
for i in range(10):
    pro = ('z%d.png'%i)
    province.append(pro)
#print(province)

for j in range(len(province)):
    image = cv2.imread(province[j],1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (1, 1), 0)
    thresh = ~(cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1])
    cv2.imshow("test",thresh)
    sum_col = sum(thresh)

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

 
    # show the output image
    cv2.imshow("Image", image)
    cv2.imwrite(('province_crop%d.jpg'%j),image)
    cv2.destroyAllWindows()























