import cv2
import sys

name = sys.argv[1]
cv2.imwrite(name, cv2.resize(cv2.imread(name), (192,192)))

