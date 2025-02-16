#%% [Imports]
from dataclasses import dataclass
from .parameter_types import ParameterType
import ast 
from pathlib import Path
import re
from enum import Enum
from typing import Optional, Union, Any #| [docs](https://docs.python.org/3/library/typing.html)
import keyword       #| [docs](https://docs.python.org/3/library/keyword.html)

# Define type aliases
type Identifier = str
type UnionType = Union[bool, int, float, str]
type UnionNumber = Union[int, float]
type UnionFilesystem = Union[str, Path]


# %% [Helper Functions]

def is_valid_identifier(name: Identifier) -> bool:
    return name.isidentifier() and not keyword.iskeyword(name)


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# %% [Main Class]

class HelpType(Enum):
    SIMPLE = "simple"
    MARKDOWN = "markdown"
    RESTRUCTURED_TEXT = "restructured_text"

@dataclass
class BaseParameter:
    """
    """
    _name: Identifier 
    _value: UnionType
    _type: ParameterType
    _help: Optional[str] = None
    _help_type: HelpType = HelpType.SIMPLE

    def __init__(self, name: Identifier, value: UnionType, param_type: ParameterType, help: Optional[str] = None):
        if not self.is_identifier(name):
            raise ValueError(f"Parameter name '{name}' is not a valid Python identifier.")
        
        self._name = name
        
        # check if the param_type is a valid value for the ParameterType enum
        if not isinstance(param_type, ParameterType):
            raise ValueError(f"Parameter type '{param_type}' is not a valid parameter type.")
        
        self._type = param_type
        
        if not self.is_valid_type(value):
            raise ValueError(f"Parameter value '{value}' is not a valid value for type '{param_type}'.")
        
        self._value = value
                
        self._help = help
        self._help_type = self.detect_help_type(help)
                        
    def __str__(self) -> str:
        return f"{self._name} = {self._value} {self._type}"
    
    def __repr__(self) -> str:
        return f"Parameter({self._name}, {self._value}, {self._type})"
    
    def is_identifier(self, name: Identifier) -> bool:
        try:
            node = ast.parse(name, mode='eval')
            if isinstance(node.body, ast.Name) and node.body.id == name:
                return True
        except SyntaxError:
            return False
        return False
    
    def is_path(self, path: UnionFilesystem) -> bool:
        if isinstance(path, Path):
            path = str(path)
        if not isinstance(path, str):
            return False
        # Define a regex pattern for invalid characters in file/directory names
        # allow for Windows drive letters (e.g. C:)
        if re.match(r'^[a-zA-Z]:\\', path):
            path = path[2:]
            
        invalid_chars = r'[<>:"|?*\x00-\x1F]'
        if re.search(invalid_chars, path):
            return False
        return True
        
    
    def is_valid_type(self, value: UnionType) -> bool:
        if self._type == ParameterType.BooleanParameter:
            return isinstance(value, bool)
        
        elif self._type == ParameterType.IntegerParameter:
            return isinstance(value, int)
        
        elif self._type == ParameterType.FloatParameter:
            return isinstance(value, float)
        
        elif self._type == ParameterType.StringParameter:
            # a string is a basic `str` type
            return isinstance(value, str)
                
        elif self._type == ParameterType.ChoiceParameter:
            # a choice value defines a list of same values 
            if type(value) == str or type(value) == int  or type(value) == float:
                return True
            else:
                return False
            
        elif self._type == ParameterType.FontNameParameter:
            # a font name is a string
            # TODO: find a way to check if the font is installed on the system
            return isinstance(value, str)
        
        elif self._type == ParameterType.FontSizeParameter:
            # a font size is a float or int
            return (isinstance(value, int)) and value >= 0
        
        elif self._type == ParameterType.TextParameter:
            # a text is a string
            return isinstance(value, str)
        
        elif self._type == ParameterType.FileNameParameter:
            # a file name is a string
            return (isinstance(value, str) or isinstance(value, Path)) and self.is_path(value)
        
        elif self._type == ParameterType.FileParameter:
            # a file name is a string
            # TODO: check is_link for files? 
            if not Path(value).exists():
                raise ValueError(f"Path '{value}' does not exist\n-> Please create file before using it as a parameter path.")
            return (isinstance(value, str) or isinstance(value, Path)) and Path(value).is_file()
        
        elif self._type == ParameterType.PathParameter:
            # a path is a string
            # TODO: check is_link for directories?
            if not Path(value).exists():
                raise ValueError(f"Path '{value}' does not exist\n-> Please create path before using it as a parameter path.")
            return (isinstance(value, str) or isinstance(value, Path)) and Path(value).is_dir()
        
        else:
            return False
        
    def detect_help_type(self, help_text: Optional[str]) -> HelpType:
        if help_text is None:
            return HelpType.SIMPLE
        if help_text.startswith("#") or help_text.startswith("*") or help_text.startswith("-"):
            return HelpType.MARKDOWN
        if help_text.startswith(".. "):
            return HelpType.RESTRUCTURED_TEXT
        return HelpType.SIMPLE
    
    @property
    def name(self) -> Identifier:
        return self._name
    
    @property
    def value(self) -> UnionType:
        return self._value
    
    
    @property
    def param_type(self) -> ParameterType:
        return self._type

    
    @property
    def help(self) -> str:
        return self._help

    @help.setter
    def help(self, value: str) -> None:
        self._help = value
        self._help_type = self.detect_help_type(value)

    @property
    def help_type(self) -> HelpType:
        return self._help_type


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

class RangeParameter(BaseParameter):
    
    _min_value: Optional[UnionNumber] = None
    _max_value: Optional[UnionNumber] = None
    _step_value: Optional[UnionNumber] = None
    _default_value: Optional[UnionNumber] = None

    def __init__(self, name: Identifier, value: UnionType, param_type: ParameterType, unit: str,  help: Optional[str] = None, min_value: Optional[UnionNumber] = None, max_value: Optional[UnionNumber] = None, step_value: Optional[UnionNumber] = None, default_value: Optional[UnionNumber] = None):
        super().__init__(name, value, param_type, help)

        value_type = type(self.value)

        if min_value is not None: 
            if not isinstance(min_value, value_type):
                raise ValueError(f"Parameter min_value '{min_value}' is not a valid value for type '{value_type}' determined by the given value.")
            
            self._min_value = min_value
        else:
            self._min_value = None
        
        if max_value is not None:
            if not isinstance(max_value, value_type):
                raise ValueError(f"Parameter max_value '{max_value}' is not a valid value for type '{value_type}' determined by the given value.")
            elif min_value and min_value > max_value:
                raise ValueError(f"Parameter min_value '{min_value}' is greater than max_value '{max_value}'.")
            
            self._max_value = max_value
        else:
            self._max_value = None
        
        if step_value is not None:
            if not isinstance(step_value, value_type):
                raise ValueError(f"Parameter step_value '{step_value}' is not a valid value for type '{value_type}' determined by the given value.")
            elif max_value and min_value and step_value > (max_value - min_value):
                raise ValueError(f"Parameter step_value '{step_value}' is greater than the range of min_value '{min_value}' and max_value '{max_value}'.")
            
            self._step_value = step_value
        else:
            self._step_value = None
        
        if default_value is not None:
            if not isinstance(default_value, value_type):
                raise ValueError(f"Parameter default_value '{default_value}' is not a valid value for type '{value_type}' determined by the given value.")
            elif max_value and default_value > max_value:
                raise ValueError(f"Parameter default_value '{default_value}' is greater than max_value '{max_value}'.")
            elif min_value and default_value < min_value:
                raise ValueError(f"Parameter default_value '{default_value}' is smaller than min_value '{min_value}'.")
            
            self._default_value = default_value
        else:
            self._default_value = None
            
        if unit and not self.is_unit(unit):
            raise ValueError(f"Parameter unit '{unit}' is not a valid unit.")
        self._unit = unit


    def __str__(self) -> str:
        return f"{self._name} = {self.value} {self._unit}"
    
    def __repr__(self) -> str:
        return f"RangeParameter({self._name}, {self.value}, {self._unit}, {self._type})"

    def is_unit(self, unit: str) -> bool:
        # TODO: implement is_unit() member based on of the given libraries or strings.
        return True

    @property
    def min_value(self) -> Optional[UnionNumber]:
        return self._min_value
    
    @property
    def max_value(self) -> Optional[UnionNumber]:
        return self._max_value
    
    @property
    def step_value(self) -> Optional[UnionNumber]:
        return self._step_value
    
    @property
    def default_value(self) -> Optional[UnionNumber]:
        return self._default_value

    @property
    def unit(self) -> str:
        return self._unit

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

class CalculationParameter(BaseParameter):
    
    _calc: Optional[str] = None
    _unit: str = None
    
    def __init__(self, name: Identifier, value: UnionType, param_type: ParameterType, unit: str, calc: Optional[str] = None, help: Optional[str] = None):
        super().__init__(name, value, param_type, help)
        
        if calc and not self.is_calculation(calc):
            raise ValueError(f"Parameter calculation '{calc}' is not a valid Python calculation.")
                
        self._calc = calc
        
        if unit and not self.is_unit(unit):
            raise ValueError(f"Parameter unit '{unit}' is not a valid unit.")
        
        self._unit = unit
        
        

    def __str__(self) -> str:
        return f"{self._name} = {self.value} {self._unit}"
    
    def __repr__(self) -> str:
        return f"CalculationParameter({self._name}, {self.value}, {self._unit}, {self._type})"

    def is_unit(self, unit: str) -> bool:
        # TODO: implement is_unit() member based on of the given libraries or strings.
        return True
    
    def is_calculation(self, calc: str) -> bool:
        check = False 
        
        try:
            tree = ast.parse(calc)
            # TODO: it should only be a simple calculation
            
            check = True
            
        except SyntaxError:
            return False
        
        return check
        
    @property
    def unit(self) -> str:
        return self._unit

    @property
    def calc(self) -> Optional[str]:
        return self._calc
