#%% [Imports]
from enum import Enum

#%% [Types]

# TODO: check if description can be replaced by unit ?

class ParameterType(Enum):
	# Core-type parameters
	BooleanParameter = 'bool'       # 
	IntegerParameter = 'integer' # if >= 0: also used for counting
	FloatParameter = 'float'     #
	StringParameter = 'string'
		
	# CAD-parameters
	ColorParameter = 'color'     # #RRGGBBAA
	AxisParameter = 'axis' # X, Y, Z 
	LocationParameter = 'location' # x,y,z 
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
	# ! ResistanceParameter = 'resistance' 
	# ! CurrentParameter = 'current'
	# ! VoltageParameter = 'voltage'
	# ! ConsumptionParameter = 'consumption' 
	# ! FrequencyParameter = 'frequency'
	
	# Specific 
	# ! ConstantParameter = 'constant'         # for constants
	ChoiceParameter = 'choice'             # Using enum
	# ! CalculationParameter = 'calculation'   #
	# ! LinearTranslationParameter = 'linear'  # Linear Function
	# ? Filter
	# ? Derivation
	# ? Integrate
	
	# Written text
	FontNameParameter = 'font-name'        # A font name (installed on system)
	FontSizeParameter = 'font-size'        # A font size
	TextParameter = 'string'               # 
	
	# File system parameter
	FileNameParameter = 'file-name'        # A file name
	FileParameter = 'file'                 # A file object 
	PathParameter = 'path-parameter'       # A path in the file system