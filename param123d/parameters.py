from .parameter_base import Parameter
from .parameter_groups import ParameterGroup

#---------------------------------------------------------------------------------------------------------------------------------------
# Core Types
#---------------------------------------------------------------------------------------------------------------------------------------


class BooleanParameter(Parameter):
    """A boolean parameter class that inherits from the Parameter class."""

    def __init__(self, name : str, value : bool, calc: Optional[str] = None, default_value : bool = False, help : str = None):
        """Initialize the BooleanParameter class."""
        min_value=False
        max_value=True
        step_value=None
        unit=None
        super().__init__(name, value, ParameterType.BooleanParameter, unit, min_value, max_value, step_value, default_value, help)
        

class IntegerParameter(Parameter):
    """An integer parameter class that inherits from the Parameter class."""

    def __init__(self, name : str, value : int, min_value : int, max_value : int, step_value : int = 1, default_value : int = 0, unit : str = None, calc: Optional[str] = None, help : str = None):
        """Initialize the IntegerParameter class."""
        super().__init__(name, value, ParameterType.IntegerParameter, unit, min_value, max_value, step_value, default_value, calc, help)
        

class FloatParameter(Parameter):
    """An float parameter class that inherits from the Parameter class."""
    
    def __init__(self, name : str, value : float, min_value : float, max_value : float, step_value : float = 0.1, default_value : float = 0.0, unit : str = None, calc: Optional[str] = None, help : str = None):
        """Initialize the FloatParameter class."""
        super().__init__(name, value, ParameterType.FloatParameter, unit, min_value, max_value, step_value, default_value, calc, help)
        

class StringParameter(Parameter):
    """A string parameter class that inherits from the Parameter class."""
    
    def __init__(self, name : str, value : str, default_value : str = '', help : str = None):
        """Initialize the StringParameter class."""
        no_unit = None 
        no_calc = None 
        no_min = None
        no_max = None
        no_step = None
        
        super().__init__(name, value, ParameterType.StringParameter, no_unit, no_min, no_max, no_step, default_value, no_calc, help)
        

#---------------------------------------------------------------------------------------------------------------------------------------
# CAD parameters
#---------------------------------------------------------------------------------------------------------------------------------------

@dataclass
class ColorParameter(StringParameter):
    """A color parameter class (`#RRGGBBAA`) that inherits from the StringParameter class."""
    
    color : str = '#000000FF'
    
    def __init__(self, name : str, value : str, default_value : str = '', help : str = None):
        """Initialize the ColorParameter class."""
        super().__init__(name, value, default_value, help)

if 0:
    pass # TODO:
	# > AxisParameter = 'axis' # X, Y, Z 
	# > LocationParameter = 'location' # x,y,z 
	# > RotationParameter = 'rotation'  #
	# > LengthParameter = 'length' # [mm]
	# > AreaParameter = 'area' # [mm^2]
	# > VolumeParameter = 'volume' # [mm^3] 
	# > MassParameter = 'mass' # [g]
	# > AngleParameter = 'angle' # 
	
#---------------------------------------------------------------------------------------------------------------------------------------
# Physical (non CAD)
#---------------------------------------------------------------------------------------------------------------------------------------

class TimeParameter(IntegerParameter):
    """ 
    A time parameter class that inherits from the IntegerParameter class.
    """
    
    def __init__(self, name : str, value : int, min_value : int, max_value : int, step_value : int = 1, default_value : int = 0, unit : str = 's', calc: Optional[str] = None, help : str = None):
        """Initialize the TimeParameter class."""
        super().__init__(name, value, min_value, max_value, step_value, default_value, unit, calc, help)
        

class SpeedParameter(FloatParameter):
    """
    A speed parameter
    """
    def __init__(self, name : str, value : float, min_value : float, max_value : float, step_value : float = 0.1, default_value : float = 0.0, unit : str = 'm/s', calc: Optional[str] = None, help : str = None):
        """Initialize the SpeedParameter class."""
        super().__init__(name, value, min_value, max_value, step_value, default_value, unit, calc, help)


class AccelerationParameter(FloatParameter):
    """
    An acceleration parameter
    """
    def __init__(self, name : str, value : float, min_value : float, max_value : float, step_value : float = 0.1, default_value : float = 0.0, unit : str = 'm/s^2', calc: Optional[str] = None, help : str = None):
        """Initialize the AccelerationParameter class."""
        super().__init__(name, value, min_value, max_value, step_value, default_value, unit, calc, help)
        

class ForceParameter(FloatParameter):
    """
    A force parameter
    """
    def __init__(self, name : str, value : float, min_value : float, max_value : float, step_value : float = 0.1, default_value : float = 0.0, unit : str = 'N', calc: Optional[str] = None, help : str = None):
        """Initialize the ForceParameter class."""
        super().__init__(name, value, min_value, max_value, step_value, default_value, unit, calc, help)
        

class TorqueParameter(FloatParameter):
    """
    A torque parameter
    """
    def __init__(self, name : str, value : float, min_value : float, max_value : float, step_value : float = 0.1, default_value : float = 0.0, unit : str = 'Nm', calc: Optional[str] = None, help : str = None):
        """Initialize the TorqueParameter class."""
        super().__init__(name, value, min_value, max_value, step_value, default_value, unit, calc, help)
        
        
class TemperatureParameter(FloatParameter):
    """
    A temperature parameter
    """
    def __init__(self, name : str, value : float, min_value : float, max_value : float, step_value : float = 0.1, default_value : float = 0.0, unit : str = '°C', calc: Optional[str] = None, help : str = None):
        """Initialize the TemperatureParameter class."""
        super().__init__(name, value, min_value, max_value, step_value, default_value, unit, calc, help)



# ! ResistanceParameter = 'resistance' 
# ! CurrentParameter = 'current'
# ! VoltageParameter = 'voltage'
# ! ConsumptionParameter = 'consumption' 
# ! FrequencyParameter = 'frequency'
	
#---------------------------------------------------------------------------------------------------------------------------------------
# Specific Types
#---------------------------------------------------------------------------------------------------------------------------------------

class ChoiceParameter(Parameter):
    """A choice parameter class that inherits from the Parameter class."""
    
    def __init__(self, name : str, choices : List[Any(str,int,float)], default_value : Any(str,int,float) = '', help : str = None):
        """Initialize the ChoiceParameter class."""
        
        no_unit = None
        no_calc = None
        no_min = None
        no_max = None
        no_step = None
        super().__init__(name, choices, ParameterType.ChoiceParameter, no_unit, no_min, no_max, no_step, default_value, no_calc, help)


# ! ConstantParameter = 'constant'         # for constants
# ! CalculationParameter = 'calculation'   #
# ! LinearTranslationParameter = 'linear'  # Linear Function
# ? Filter
# ? Derivation
# ? Integrate
	
#---------------------------------------------------------------------------------------------------------------------------------------
# Written Test Types
#---------------------------------------------------------------------------------------------------------------------------------------


class FontParameter(StringParameter):
    """A font parameter class that inherits from the Parameter class."""

    def __init__(self, name : str, value : str, default_value : str = '', help : str = None):
        """Initialize the FontParameter class."""
        super().__init__(name, value, default_value, help)
        
    #TODO: how to get the installed fonts -- probably FontManager from ocp/build123d

            

class FontSizeParameter(Parameter):
    """A font size parameter class that inherits from the Parameter class."""
    
    def __init__(self, name : str, value : int, min_value : int, max_value : int, step_value : int = 1, default_value : int = 0, unit : str = 'pt', calc: Optional[str] = None, help : str = None):
        """Initialize the FontSizeParameter class."""
        super().__init__(name, value, ParameterType.FontSizeParameter, unit, min_value, max_value, step_value, default_value, calc, help)
        

class TextParameter(StringParameter):
    """A text parameter class that inherits from the StringParameter class."""
    
    def __init__(self, name : str, value : str, default_value : str = '', help : str = None):
        """Initialize the TextParameter class."""
        super().__init__(name, value, default_value, help)
	

#---------------------------------------------------------------------------------------------------------------------------------------
# File system parameter
#---------------------------------------------------------------------------------------------------------------------------------------

class FileNameParameter(Parameter):
    """A file parameter class that inherits from the Parameter class."""
    
    def __init__(self, name : str, value : str, default_value : str = '', help : str = None):
        """Initialize the FileParameter class."""
        no_unit = None 
        no_calc = None 
        no_min = None
        no_max = None
        no_step = None
        
        super().__init__(name, value, ParameterType.FileNameParameter, no_unit, no_min, no_max, no_step, default_value, no_calc, help)


class FileParameter(Parameter):
    """A file parameter class that inherits from the Parameter class."""
    
    def __init__(self, name : Any(str,Path), value : str, default_value : str = '', help : str = None):
        """Initialize the PathParameter class."""
        no_unit = None 
        no_calc = None 
        no_min = None
        no_max = None
        no_step = None
        
        super().__init__(name, value, ParameterType.FileParameter, no_unit, no_min, no_max, no_step, default_value, no_calc, help)


class PathParameter(Parameter):
    """A path parameter class that inherits from the Parameter class."""
    
    def __init__(self, name : str, value : str, default_value : str = '', help : str = None):
        """Initialize the PathParameter class."""
        no_unit = None 
        no_calc = None 
        no_min = None
        no_max = None
        no_step = None
        
        super().__init__(name, value, ParameterType.PathParameter, no_unit, no_min, no_max, no_step, default_value, no_calc, help)
        
                