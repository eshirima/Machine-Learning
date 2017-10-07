import matplotlib.pyplot as plt

from data import Data
from scipy import stats
from datetime import datetime
from ordinary_least_squares import OLS

total_points = 20

points = Data()
points.generate(total_points)

print points.x_values()
print points.y_values()

model = OLS(points)

start = datetime.now()
my_slope, my_intercept = model.calculate_line()
print 'Model duration: ', datetime.now() - start

start = datetime.now()
scipy_slope, scipy_intercept, _, _, _ = stats.linregress(points.x_values(), points.y_values())
print 'Scipy duration: ', datetime.now() - start

print 'Personal: ', my_slope, my_intercept
print 'Scipy: ', scipy_slope, scipy_intercept

plt.scatter(points.x_values(), points.y_values())
plt.xlabel('X')
plt.ylabel('Y')

x_min, x_max = plt.xlim()

my_y_max = my_slope * (x_max - x_min) + my_intercept
scipy_y_max = scipy_slope * (x_max - x_min) + scipy_intercept

line1, = plt.plot([x_min, x_max], [my_intercept, my_y_max], 'b', label='Model')
plt.title(str(total_points) + ' points generated')

first_legend = plt.legend(handles=[line1], loc=1)
# Add the legend manually to the current Axes.
ax = plt.gca().add_artist(first_legend)

# add some room for the text
plt.gca().set_position((.1, .3, .8, .6))

model_text = 'Model: $y=' + str(my_slope) + 'x' + '+' + str(my_intercept) + '$'
scipy_text = 'Scipy: $y=' + str(scipy_slope) + 'x' + '+' + str(scipy_intercept) + '$'

plt.figtext(.02, .02, model_text)
plt.figtext(.02,.05, scipy_text)

plt.show()