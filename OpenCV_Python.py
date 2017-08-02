import numpy as np
import cv2



fname = r'C:\Users\HunPC\Desktop\Chrysanthemum.jpg'
flower = cv2.imread(fname,1)
cv2.imshow('flower',flower)
cv2.waitKey()