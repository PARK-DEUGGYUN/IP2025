import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('lenna.png',0)
edges1 = cv2.Canny(img,50,200)
edges2 = cv2.Canny(img,50,150)
edges3 = cv2.Canny(img,50,100)
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(edges1,cmap = 'gray')
plt.title('50,200'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(edges2,cmap = 'gray')
plt.title('50,150'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(edges3,cmap = 'gray')
plt.title('50,100'), plt.xticks([]), plt.yticks([])
plt.show()