import cv2
import warnings
import numpy as np

class SVD:
    # takes a grey scale image and computes its components
    def __init__(self, image):

        self.image = image
        self.U, self.S, self.V = None, None, None

    def compute(self):
        self.U, self.S, self.V = np.linalg.svd(self.image)
        return self.U, self.S, self.V

    def __reconstruct_normal__(self, iterations):
        index = 0
        recon_matrix = np.zeros(self.image.shape)

        while index < iterations:
            row_v = self.V[index].reshape(1, self.V.shape[1])
            column_u = self.U[:, index].reshape(self.U.shape[0], 1)

            product = np.multiply(row_v, column_u)

            current = np.multiply(self.S[index], product)

            recon_matrix = np.add(recon_matrix, current)

            visual = recon_matrix.astype(np.uint8)

            title = 'Image ' + str(index)

            cv2.imshow(title, visual)

            index += 1

        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()

    #TODO: Perform SVD for each channel independently
    def __reconstruct_colour__(self, iterations):

        index = 0
        reconMatrix = np.zeros(self.image.shape)

        while index < iterations:

            # row_v = self.V[index].reshape(1, self.V.shape[1])
            # column_u = self.U[:, index].reshape(self.U.shape[0], 1)
            #
            # product = np.multiply(row_v, column_u)
            #
            # current = np.multiply(self.S[index], product)
            #
            # recon_matrix = np.add(recon_matrix, current)

            red_row_v = self.red_V[index].reshape(1, self.red_V.shape[1])
            red_column_u = self.red_U[:, index].reshape(self.red_U.shape[0], 1)

            green_row_v = self.green_V[index].reshape(1, self.green_V.shape[1])
            green_column_u = self.green_U[:, index].reshape(self.green_U.shape[0], 1)

            blue_row_v = self.blue_V[index].reshape(1, self.blue_V.shape[1])
            blue_column_u = self.blue_U[:, index].reshape(self.blue_U.shape[0], 1)

            red_product = np.multiply(red_row_v, red_column_u)
            green_product = np.multiply(green_row_v, green_column_u)
            blue_product = np.multiply(blue_row_v, blue_column_u)

            red_product = np.multiply(self.S[index], red_product)
            green_product = np.multiply(self.S[index], green_product)
            blue_product = np.multiply(self.S[index], blue_product)

            merged_image = cv2.merge(blue_product, green_product, red_product)

            reconMatrix = np.add(reconMatrix, merged_image)

            title = 'Image ' + str(index)

            visual = reconMatrix.astype(np.uint8)

            cv2.imshow(title, visual)

            index += 1

        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()

    #TODO: Finish the final setup
    def reconstruct(self, iterations=5):

        if iterations >= len(self.S) or iterations < 0:
            error_text = 'Invalid number of iterations used. Value was reset to {}; image max'.format(len(self.S))
            warnings.warn(error_text)
            iterations = len(self.S)

        # if None in (self.U, self.S, self.V):
        #     raise SystemExit('U, S or V is empty. Make sure compute() was called before reconstruction.')

        if self.U is None or self.S is None or self.V is None:
            raise SystemExit('U, S or V is empty. Make sure compute() was called before reconstruction.')

        self.__reconstruct_normal__(iterations)
