import numpy as np

class Data:
    def __init__(self):
        self._total_points = None
        self._x = np.empty(1, dtype=float)
        self._y = np.empty(1, dtype=float)

    def generate(self, total_points):
        self._total_points = total_points
        # self._x = np.random.uniform(low=1.0, high=1000.0, size=total_points)
        # self._y = np.random.uniform(low=1.0, high=1000.0, size=total_points)

        self._x = np.random.random(total_points)
        self._y = np.random.random(total_points)

    def x_values(self):
        return self._x

    def y_values(self):
        return self._y

    def count(self):
        return self._total_points