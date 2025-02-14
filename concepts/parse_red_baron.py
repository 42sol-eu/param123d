'''
RedBaron is a python library that allows you to manipulate the Abstract Syntax Tree (AST) of python code.

'''

from redbaron import RedBaron  						# https://redbaron.readthedocs.io/en/latest/



code = '''
n = 42
with ParameterGroup('Box') as pars:
    a = IntegerParameter('a', 12, calc=n/360)
    pars('a').desc = '[mm] length'
    pars('a').help = 'A simple parameter'
    FontParameter('Title', "font_name")

    a = AngleParameter('a', 12, calc=n/360,
        unit='degree',
        help='The angle of the lines [a] and [b].')
'''

tree = ast.parse(code)
for count, node in enumerate(ast.walk(tree)):
    if isinstance(node, ast.Assign):
        print(f"L {node.lineno} to {node.end_lineno}: {'_'*42}")
        print(count, ast.dump(node,indent=4))
    elif isinstance(node, ast.With):
        print(f"L {node.lineno} to {node.end_lineno}: {'#'*42}")
        print(count, ast.dump(node,indent=4))    	
    else:
        print(f"- {type(node)} {'-'*42}")
        if 0:
            print(count, ast.dump(node,indent=4))        

def single_lines():
    for count, line in enumerate(code.split('\n')):
        eval1 = ast.parse(line, 'eval')
        print(count, ast.dump(eval1,indent=4))
