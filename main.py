from Graph import plot_graph, plot_random_distribution_graph
from math import sin
import numpy

# x = numpy.arange(0, 314)
# for i in x:
#     print(eval('lambda: ' + 'sin(i/100)')())

plot_graph('sin(x/2) * e^x', -2, 8)
plot_graph('gasgsa', -10, 10)