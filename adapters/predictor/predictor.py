import numpy as np
import cv2
from matplotlib import pyplot as plt
# Read image
im = cv2.imread('../../asserts/1.jpg', cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(im,50,255)
indices = np.where(edges != [0])
coordinates = np.array(list(zip(indices[0], indices[1])))

print coordinates
a=coordinates[0]
b=coordinates[150]
dist = np.linalg.norm(a-b)
print dist
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow("image",edges )
cv2.waitKey(0)