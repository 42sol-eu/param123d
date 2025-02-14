#%% [Imports]
import pint                                      # https://pint.readthedocs.io/en/stable/
from pint import UnitRegistry

#%% [Setup]
preferred_units = [ 
	registry.meter,  # distance      L
    registry.gramm,  # mass          M
    registry.s,  # duration      T
    registry.celcius,  # temperature   Θ
    registry.N,  # force         L M T^-2
    registry.W,  # power         L^2 M T^-3
]

registry = UnitRegistry(autoconvert_offset_to_baseunit=True)
registry.default_preferred_units(preferred_units)

mm = registry.millimeters
m   = registry.meter
s   = registry.second
min = registry.minute

#%% [Examples]

# speed.to('kilometer/hour')
# speed.ito( type )
# object.to_compact()
# object.to_base_units() / .ito_base_uints()
# used with `to_preferred(preferred_units)`

# - String parsing
Q_ = registry.Quantity
Q_(2.54, 'centimeter')

input = '10 m 12 cm'
pattern = '{meter} m {centimeter} cm'
registry.parse_pattern(input, pattern, many=True )

#%% [Modul setup]
## Setup in __init__.py in your projects
if 0:
    from pint import UnitRegistry
    registry = UnitRegistry()
    Q_ = registry.Quantity

#%% [Modul usage]
## in the using modules
if 0:
    from . import registry, Q_

    length = 10 * registry.meter
    my_speed = Q_(20, 'm/s')
