""" Import Packages """
import os
import cv2
import numpy as np
from tkinter import filedialog


""" Functions and Variables """


def nothing(x):
    pass


def get_Threshold():

    cv2.namedWindow("Threshold")

    cv2.createTrackbar("Max", "Threshold", 0, 255, nothing)

    while(1):

        img = cv2.imread(file_path, 0)

        scale_percent = 60
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)

        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        hul = cv2.getTrackbarPos("Max", "Threshold")

        ret, thresh4 = cv2.threshold(img, hul, 255, cv2.THRESH_TOZERO)

        cv2.imshow("Threshold", thresh4)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
    return hul


""" Main Programme """
default_dir = 'D:/'
file_path = filedialog.askopenfilename(
    title=u'choose file', initialdir=(os.path.expanduser(default_dir)))
print('After choose threshold, press \"ESC\" to return the threshold number')
th = get_Threshold()
print(th)
