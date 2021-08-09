import numpy as np

available_replacements = {'sin': 'np.sin', 'cos': 'np.cos', 'sh': 'np.sinh', 'csh': 'np.cosh',
                          'lg': 'np.log10', 'ln': 'np.log2', 'log': 'np.log', 'tg': 'np.tan',
                          'th': 'np.tanh', '^': '**', ':': '/', ' ': ''}


# todo make a solid parser
def parse_expr(expression: str):
    for replacement in available_replacements.keys():
        expression = expression.replace(replacement, available_replacements[replacement])
    return expression
