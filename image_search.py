import numpy as np
import cv2
import os

orb = cv2.ORB_create()
img1 = cv2.imread(r'C:\Users\HunPC\Desktop\img\img.jpg',cv2.IMREAD_GRAYSCALE)
kp1, des1 = orb.detectAndCompute(img1, None)

def featureMatching():
    for (path,dir,files) in os.walk("c:/Users\HunPC\Desktop\year2011") :
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.jpg':
                img2 = cv2.imread(path + '/' + filename ,cv2.IMREAD_GRAYSCALE)
                res = None

                                
                kp2, des2 = orb.detectAndCompute(img2, None)

                bf = cv2.BFMatcher(cv2.NORM_HAMMING ,crossCheck = True)
                matches = bf.match(des1,des2)

                matches = sorted(matches, key= lambda x:x.distance)
                res = cv2.drawMatches(img1,kp1,img2,kp2,matches[:30] , res ,flags = 0)

                cv2.imshow('FeatureMatching' ,res)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
featureMatching()