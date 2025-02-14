''' = nice123d.parser

parameter-parser
  +-> ast

Using the `abstract syntax tree` to analyze the code for `ParameterGroup` and `{Type}Parameter`.

It is advisable to:
	1. Use `with` block with `ParameterGroup()` in the main context.
	2. Use the `with ParameterGroup() as {name}:` to reference the parameters later `{name}.{parameter_name}`, like `pars.width` 
	3. Use `{Type}Parameter()` in the with-block
	4. Use assignments for parameters if you need to reference them in later calculations.
	5. Use mainly parameter definitions in the `with` block with the `ParameterGroup` definition. (`ast` should work mostly fine with other code, but it is not recommendet to mix your parameters with functional code)
  6. Use the best fitting type for you parameter, selectig more specific parameters where ever possible.
  7. Be aware of the `calc={expression}` parameter and the restrictions, that you are allowed to use inside the `calc`-expression.
  8. Be aware of the possible usage of global variables to calcualate you parameter values.
  9. Parameters can use validator functions
  10. Be aware of parameter-sets that are stored as `yaml` files in the model folder. You can store the parameter-sets
  11. Avoid additional logic or statements in the `with` block or around the `{Type}Parameter` definitions like `if` or `for` because the parser will not be able to register this statements logic or show it in the user interface.
'''

import  ast 		                         # https://docs.python.org/3/library/ast.html
from redbaron import RedBaron  # https://redbaron.readthedocs.io/en/latest/

# %%[] Unit type implementations ... 
## https://kdavies4.github.io/natu/

import pint                                      # https://pint.readthedocs.io/en/stable/
from pint import UnitRegistry
units = UnitRegistry()
mm = units.millimeters
m = units.meter
s = units.second
min = units.minute
# speed.to('kilometer/hour')
# speed.ito( type )
# object.to_compact()
# object.to_base_units() / .ito_base_uints()
preferred_units = [ 
		    ureg.meter,  # distance      L
       ureg.gramm,  # mass          M
       ureg.s,  # duration      T
       ureg.celcius,  # temperature   Θ
       ureg.N,  # force         L M T^-2
       ureg.W,  # power         L^2 M T^-3
    ]
# used with `to_preferred(preferred_units)`
registry = default_preferred_units = preferred_units
registry.autoconvert_to_preferred = True

# - String parsing
Q_ = registry.Quantity
Q_(2.54, 'centimeter')

input = '10 m 12 cm'
pattern = '{meter} m {centimeter} cm'
registry.parse_pattern(input, pattern, many=True )

## Setup in __init__.py in your projects
from pint import UnitRegistry
ureg = UnitRegistry()
Q_ = ureg.Quantity

## in the using modules
from . import ureg, Q_

length = 10 * ureg.meter
my_speed = Q_(20, 'm/s')


#%% [Types]
from enum import Enum


# TODO: check if description can be replaced by unit ?

class ParameterType(Enum):
	# Core-type parameters
	BoolParameter = 'bool'       # 
	IntegerParameter = 'integer' # if >= 0: also used for counting
	FloatParameter = 'float'     #
	StringParameter = 'string'
		
	# CAD-parameters
	IdentifierParameter = 'identifier' # A name or identifier
	AxisParameter = 'axis' # X, Y, Z 
	LocationParameter = 'loctation' # x,y,z 
	RotationParameter = 'rotation'  #
	LengthParameter = 'length' # [mm]
	AreaParameter = 'area' # [mm^2]
	VolumeParameter = 'volume' # [mm^3] 
	MassParameter = 'mass' # [g]
	AngleParameter = 'angle' # 
	
	# Physical (non CAD)
	TimeParameter = 'time' 
	SpeedParameter = 'speed'
	AccelerationParameter = 'acceleration'
	ForceParameter = 'force'
	TorqueParameter = 'torque' 
	TemperatureParameter = 'temperature'
	ResistanceParameter = 'resistance' 
	CurrentParameter = 'current'
	VoltageParameter = 'voltage'
	ConsumptionParameter = 'consumption' 
	FrequencyParameter = 'frequency'
	
	# Specific 
	ConstantParameter = 'constant'         # for constants
	ChoiceParameter = 'choice'             # Using enum
	CalculationParameter = 'calculation'   #
	LinearTranslationParameter = 'linear'  # Linear Function
	# ? Filter
	# ? Derivation
	# ? Integrate
	
	# Written text
	FontNameParameter = 'font-name'        # A font name (installed on system)
	FontSizeParameter = 'font-size'        # A font size
	TextParameter = 'string'               # 
	
	# File system parameter
	FileParameter = 'file-name'            # A file name 
	PathParameter = 'path-parameter'       # A path in the file system

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
