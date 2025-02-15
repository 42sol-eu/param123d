from .parameter_base import BaseParameter, RangeParameter, CalculationParameter
from .parameter_types import ParameterType
from .parameter_groups import ParameterGroup
from nicegui import ui
from pathlib import Path
from typing import Any, List, Optional, Union
from dataclasses import dataclass

#---------------------------------------------------------------------------------------------------------------------------------------
# Core Types
#---------------------------------------------------------------------------------------------------------------------------------------


class BooleanParameter(BaseParameter):
    """A boolean parameter class that inherits from the Parameter class."""

    def __init__(self, name : str, value : bool, help : str = None):
        """Initialize the BooleanParameter class."""
        super().__init__(name, value, ParameterType.BooleanParameter, help)
        
    def create_ui(self):
        label  = ui.label(self.name).props('w-full')
        switch = ui.switch()
        switch.set_value(self.value)
        
        help   = ui.markdown(self.help)
        
        return (label, switch, help)

    @property
    def help(self):
        return self._help
    
    @help.setter
    def set_help(self, value : str):
        self._help = value

class IntegerParameter(RangeParameter):
    """An integer parameter class that inherits from the Parameter class."""

    def __init__(self, name : str, value : int,  unit : str = None, help : str = None, min_value : int = None, max_value : int = None, step_value : int = 1, default_value : int = 10):
        """Initialize the IntegerParameter class."""
        super().__init__(name, value, ParameterType.IntegerParameter, unit, help, min_value, max_value, step_value, default_value)
        
    def dict_valid(self : Any) -> bool:
        """Validate the value to ensure it is within the specified range."""
        
        validation = {}
        # validation['not int'] = lambda value: isinstance(value, int)
        validation['too small'] = lambda value: value >= self.min_value
        validation['too big'] = lambda value: value <= self.max_value
        validation['not in step'] = lambda value: (value-self.min_value) % self.step_value == 0
        return validation
    
    def create_ui(self):
        label  = ui.label(self.name).props('w-full')
        main = ui.number(validation=self.dict_valid())
        main.set_value(self.value)
        
        help   = ui.markdown(self.help + f'\n- Min: {self.min_value},\n- Max: {self.max_value}')
        
        return (label, main, help)

    @property
    def help(self):
        return self._help
    
    @help.setter
    def help(self, value : str):
        self._help = value

class FloatParameter(RangeParameter):
    """An float parameter class that inherits from the Parameter class."""
    
    def __init__(self, name : str, value : float, unit : str = None, help : str = None, min_value : float = 0.0, max_value : float = 100.0, step_value : float = 0.1, default_value : float = 0.0):
        """Initialize the FloatParameter class."""
        super().__init__(name, value, ParameterType.FloatParameter, unit, help,  min_value, max_value, step_value, default_value)
        
    # TODO: implement FloatParameter.create_ui()

class StringParameter(BaseParameter):
    """A string parameter class that inherits from the Parameter class."""
    
    def __init__(self, name : str, value : str, help : str = None):
        """Initialize the StringParameter class."""
        
        super().__init__(name, value, ParameterType.StringParameter, help)
        

#---------------------------------------------------------------------------------------------------------------------------------------
# CAD parameters
#---------------------------------------------------------------------------------------------------------------------------------------

@dataclass
class ColorParameter(BaseParameter):
    """A color parameter class (`#RRGGBBAA`) that inherits from the StringParameter class."""
    
    color : str = '#000000FF'
    
    def __init__(self, name : str, value : str, help : str = None):
        """Initialize the ColorParameter class."""
        super().__init__(name, value, ParameterType.ColorParameter, help)

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
# Specific Types
#---------------------------------------------------------------------------------------------------------------------------------------

class ChoiceParameter(BaseParameter):
    """A choice parameter class that inherits from the Parameter class."""
    _choices : List[Union[str, int, float]]
    
    def __init__(self, name: str, choices: List[Union[str, int, float]], default_value: Union[str, int, float] = '', help: str = None):
        """Initialize the ChoiceParameter class."""
        self._choices = choices    
        super().__init__(name,  self._choices[0], ParameterType.ChoiceParameter, help)
        
    # TODO: implement ChoiceParameter.create_ui()
    


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
    _default_value : str = 'Arial'
    
    def __init__(self, name : str, value : str, default_value : str = 'Arial', help : str = None):
        """Initialize the FontParameter class."""
        self._default_value = default_value
        
        super().__init__(name, value, help)
        
    #TODO: how to get the installed fonts -- probably FontManager from ocp/build123d

            

class FontSizeParameter(BaseParameter):
    """A font size parameter class that inherits from the Parameter class."""
    _unit : str = 'Pt'
    
    def __init__(self, name : str, value : int, unit : str = 'pt', help : str = None):
        """Initialize the FontSizeParameter class."""
        self._unit = unit
        super().__init__(name, value, ParameterType.FontSizeParameter, help)
        
    @property
    def unit(self):
        return self._unit
        

class TextParameter(StringParameter):
    """A text parameter class that inherits from the StringParameter class."""
    
    def __init__(self, name : str, value : str, help : str = None):
        """Initialize the TextParameter class."""
        super().__init__(name, value, default_value, help)
	

#---------------------------------------------------------------------------------------------------------------------------------------
# File system parameter
#---------------------------------------------------------------------------------------------------------------------------------------

class FileNameParameter(BaseParameter):
    """A file parameter class that inherits from the Parameter class."""
    
    def __init__(self, name : str, value : str, default_value : str = '', help : str = None):
        """Initialize the FileParameter class."""
        no_unit = None 
        no_calc = None 
        
        super().__init__(name, value, ParameterType.FileNameParameter, no_unit, no_calc, help)


class FileParameter(BaseParameter):
    """A file parameter class that inherits from the Parameter class."""
    
    def __init__(self, name: Union[str, Path], value: str, help: str = None):
        """Initialize the FileParameter class."""
        no_unit = '' 
        no_calc = None 
        
        super().__init__(name, value, ParameterType.FileParameter, no_unit, no_calc, help)


class PathParameter(BaseParameter):
    """A path parameter class that inherits from the Parameter class."""
    
    def __init__(self, name : str, value : str, default_value : str = '', help : str = None):
        """Initialize the PathParameter class."""
        
        super().__init__(name, value, ParameterType.PathParameter, no_unit, no_calc, help)


