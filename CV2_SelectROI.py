""" Import Modules """
import cv2
from tkinter import filedialog

""" Functions and Variables """

""" Main Programme """
default_dir = 'D:/'
file_path = filedialog.askopenfilename(
    title=u'choose file', initialdir=(os.path.expanduser(default_dir)))
img = cv2.imread(file_path, 0)

showCrosshair = False
fromCenter = False

cv2.namedWindow("Image")
ROI = cv2.selectROI("Image", img, showCrosshair, fromCenter)
print(ROI)

imCrop = img[int(ROI[1]):int(ROI[1]+ROI[3]), int(ROI[0]):int(ROI[0]+ROI[2])]

cv2.namedWindow("Colony")
cv2.imshow("Colony", imCrop)
cv2.waitKey(0)
cv2.destroyAllWindows()
