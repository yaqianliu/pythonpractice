#将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
# -*- coding: utf-8 -*-

import numpy as np
import cv2

basic_img = cv2.imread('weicoimg3.jpg',3) # read in RGB

height,width,channels = basic_img.shape
print(basic_img.shape)
r = 30
cv2.circle(basic_img,(int(height-r),r),r,(0,0,255),thickness=-2,lineType=8)
font=cv2.FONT_HERSHEY_SIMPLEX
# specre = basic_img[int(width*3/4):int(height),0:int(height/4)]
cv2.putText(basic_img,'3',(int(height- int(r*5/3)),int(r*5/3)),font,2,(255,255,255),thickness=3,lineType=cv2.LINE_AA)

cv2.imshow('weicochange.jpg',basic_img)
cv2.imwrite('weicochange.jpg',basic_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

