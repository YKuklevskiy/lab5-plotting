available_replacements = {'sin': 'math.sin', 'cos': 'math.cos', 'sh': 'math.sinh', 'csh': 'math.cosh',
                          'lg': 'math.log10', 'ln': 'math.log2', 'log': 'math.log', '^': '**', ':': '/', ' ': ''}


def parse_expr(expression: str):
    for replacement in available_replacements.keys():
        expression = expression.replace(replacement, available_replacements[replacement])
    return expression