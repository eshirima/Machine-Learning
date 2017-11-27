from svd import *

image = cv2.imread('obama.jpg')
grey = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cv2.imshow('Obama', grey)

# sample = np.array([[0.96, 1.72], [2.28, 0.96]])
svd = SVD(grey)

svd.compute()

# print 'Grey', grey.shape
# print U.shape, V.shape, s.shape
# print U.shape[0], V.shape[0], s.shape[0]
#
# print 'SAMPLE: ', sample
# print 'U contents: ', U
# print 'S contents: ', s
# print 'V contents: ', V

svd.reconstruct(iterations=40)

# S = np.zeros(grey.shape, dtype=int)
# S[:grey.shape[0], :grey.shape[0]] = np.diag(s)
#
# # TODO: At some point, cut the elements which are smaller than a set threshold
# # TODO: For U, take the 71 col for V take the 71 row
#
# reconA = np.round(np.dot(np.dot(U, S), V), 0).astype(np.uint8)
#
# cv2.imshow('U', U)
# cv2.imshow('s', s)
# cv2.imshow('V', V)
# cv2.imshow('Grey', grey)
# cv2.imshow('Main', image)
# cv2.imshow('Recon', reconA)

key = cv2.waitKey(0)

if key == 27:
    cv2.destroyAllWindows()