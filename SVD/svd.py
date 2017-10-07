import cv2
import numpy as np
import tensorflow as tf

# numpy_matrix = np.array([[3, 2, 2], [2, 3, -2]])
#
# numpy_u, numpy_s, numpy_v = np.linalg.svd(numpy_matrix)
#
# print numpy_matrix
# print 'U:', numpy_u, 'shape:', numpy_u.shape
# print 'S:', numpy_s, 'shape:', numpy_s.shape
# print 'V:', numpy_v, 'shape:', numpy_v.shape
#
# reconstruction = numpy_u * numpy_s * numpy_v
# print 'Reco:', reconstruction

class SVD:
    def __init__(self, image):
        self.image = image
        self.U = None
        self.S = None
        self.V = None

    def compute(self):
        self.U, self.S, self.V = np.linalg.svd(self.image)
        return self.U, self.S, self.V

    def reconstruct(self):
        for element in self.S:
            print element

image = cv2.imread('obama.jpg')
grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
grey_frame = np.zeros(grey.shape, np.uint8)

cv2.imwrite('grey.jpg', grey)

print grey
print 'Shape', grey.shape

U, s, V = np.linalg.svd(grey)

print U.shape, V.shape, s.shape
print U.shape[0], V.shape[0], s.shape[0]

S = np.zeros(grey.shape, dtype=int)
S[:260, :260] = np.diag(s)

# TODO: At some point, cut the elements which are smaller than a set threshold
# TODO: For U, take the 71 col for V take the 71 row

reconA = np.round(np.dot(np.dot(U, S), V), 0).astype(np.uint8)

cv2.imshow('U', U)
cv2.imshow('s', s)
cv2.imshow('V', V)
cv2.imshow('Grey', grey)
cv2.imshow('Main', image)
cv2.imshow('Recon', reconA)

key = cv2.waitKey(0)

if key == 27:
    cv2.destroyAllWindows()