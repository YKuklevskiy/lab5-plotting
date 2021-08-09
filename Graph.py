import matplotlib.pyplot as plt
from sys import exc_info
import numpy as np
from numpy import e, pi
from MathParser import parse_expr


# plots a function of type y = f(x), accepts f(x) in string form as input
def plot_graph(y_expression: str, start, finish, density=200):
    x_range = np.linspace(start, finish, density)
    # print(y_expression)
    y_parsed_expression = parse_expr(y_expression)
    # print(y_parsed_expression)

    try:
        f = eval('lambda x: ' + y_parsed_expression)
        # y_range = [f(x) for x in x_range]
        y_range = f(x_range)
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
