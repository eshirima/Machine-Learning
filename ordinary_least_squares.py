class OLS:
    def __init__(self, points):
        self._x = points.x_values()
        self._y = points.y_values()
        self._total_points = points.count()
        self._slope, self._intercept = None, None
        self._x_average, self._y_average, = None, None

    def _x_values_average(self):

        if self._x_average is None:
            summation = 0.0

            for element in self._x:
                summation += element

            # TODO: division by zero risk
            self._x_average = summation / self._total_points

    def _y_values_average(self):

        if self._y_average is None:
            summation = 0.0

            for element in self._y:
                summation += element

            # TODO: division by zero risk
            self._y_average = summation / self._total_points

    def _calculate_slope(self):

        if self._slope is None:
            numerator_sum, denominator_sum = 0.0, 0.0

            for index in range(0, self._total_points):
                product = (self._x[index] - self._x_average) * (self._y[index] - self._y_average)
                numerator_sum += product

                difference = (self._x[index] - self._x_average)
                denominator_sum += pow(difference, 2)

            # TODO: division by zero risk
            self._slope = numerator_sum / denominator_sum

    def _calculate_intercept(self):

        if self._intercept is None:
            self._intercept = self._y_average - (self._slope * self._x_average)

    def calculate_line(self):

        self._x_values_average()
        self._y_values_average()

        self._calculate_slope()
        self._calculate_intercept()

        return self._slope, self._intercept