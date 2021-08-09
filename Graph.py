import matplotlib.pyplot as plt
import math
from math import pi, e
from sys import exc_info
import numpy
from MathParser import parse_expr


# plots a function of type y = f(x), accepts f(x) in string form as input
def plot_graph(y_expression: str, start, finish):
    x_range = numpy.linspace(start, finish, 250)
    # print(y_expression)
    y_parsed_expression = parse_expr(y_expression)
    # print(y_expression)

    try:
        f = eval('lambda x: ' + y_parsed_expression)
        y_range = [f(x) for x in x_range]
        # print('\n'.join([str(j) for j in y_range]))
        plt.title(f"y = {y_expression}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.plot(x_range, y_range)
        plt.show()
    except Exception:
        print("Calculation error for function")
        print(exc_info())
        return 1
    pass


def plot_random_distribution_graph():
    pass
