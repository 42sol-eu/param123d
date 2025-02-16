import pytest
from pathlib import Path
from param123d.parameter_base import BaseParameter, RangeParameter, CalculationParameter, HelpType
from param123d.parameter_types import ParameterType

# FILE: test_parameter_base.py
@pytest.fixture
def valid_file_path():
    return str(Path(__file__).parent / "test_file.py")

@pytest.fixture
def invalid_file_path():
    return str(Path(__file__).parent / "invalid_file.py")


def test_base_parameter_is_valid_type(valid_file_path, invalid_file_path):
    param = BaseParameter("test_bool", True, ParameterType.BooleanParameter)
    assert param.is_valid_type(True) == True
    assert param.is_valid_type(1) == False

    param = BaseParameter("test_int", 1, ParameterType.IntegerParameter)
    assert param.is_valid_type(1) == True
    assert param.is_valid_type(1.0) == False

    param = BaseParameter("test_float", 1.0, ParameterType.FloatParameter)
    assert param.is_valid_type(1.0) == True
    assert param.is_valid_type(1) == False

    param = BaseParameter("test_str", "test", ParameterType.StringParameter)
    assert param.is_valid_type("test") == True
    assert param.is_valid_type(1) == False

    param = BaseParameter("test_choice", 1, ParameterType.ChoiceParameter)
    assert param.is_valid_type(1) == True
    assert param.is_valid_type(4.2) == True
    assert param.is_valid_type("string") == True
    assert param.is_valid_type([1, 2, 3]) == False

    param = BaseParameter("test_font_name", "Arial", ParameterType.FontNameParameter)
    assert param.is_valid_type("Arial") == True
    assert param.is_valid_type(1) == False

    param = BaseParameter("test_font_size", 12, ParameterType.FontSizeParameter)
    assert param.is_valid_type(12) == True
    assert param.is_valid_type(-12) == False

    param = BaseParameter("test_text", "Hello", ParameterType.TextParameter)
    assert param.is_valid_type("Hello") == True
    assert param.is_valid_type(1) == False

    param = BaseParameter("test_file_name", valid_file_path, ParameterType.FileNameParameter)
    assert param.is_valid_type(valid_file_path) == True
    assert param.is_valid_type(1) == False
    assert param.is_valid_type('1:4') == False
    

    param = BaseParameter("test_file", valid_file_path, ParameterType.FileParameter)
    assert param.is_valid_type(valid_file_path) == True 
    # assert param.is_valid_type(invalid_file_path) == False

    param = BaseParameter("test_path", Path(valid_file_path).parent, ParameterType.PathParameter)
    assert param.is_valid_type(Path(valid_file_path).parent) == True 

def test_range_parameter_is_valid_type():
    param = RangeParameter("test_range", 10, ParameterType.IntegerParameter, "m", min_value=0, max_value=20)
    assert param.is_valid_type(10) == True
    assert param.is_valid_type(30.0) == False

def test_calculation_parameter_is_valid_type():
    param = CalculationParameter("test_calc", 10, ParameterType.IntegerParameter, "m", calc="5 + 5")
    assert param.is_valid_type(10) == True
    assert param.is_valid_type("10") == False

def test_detect_help_type_simple():
    param = BaseParameter(name="param1", value=42, param_type=ParameterType.IntegerParameter, help="This is a simple help text.")
    assert param.help_type == HelpType.SIMPLE

def test_detect_help_type_markdown():
    param = BaseParameter(name="param2", value=42, param_type=ParameterType.IntegerParameter, help="# This is a markdown help text.")
    assert param.help_type == HelpType.MARKDOWN
    
    param = BaseParameter(name="param3", value=42, param_type=ParameterType.IntegerParameter, help="* This is a markdown help text.")
    assert param.help_type == HelpType.MARKDOWN
    
    param = BaseParameter(name="param4", value=42, param_type=ParameterType.IntegerParameter, help="- This is a markdown help text.")
    assert param.help_type == HelpType.MARKDOWN

def test_detect_help_type_restructured_text():
    param = BaseParameter(name="param5", value=42, param_type=ParameterType.IntegerParameter, help=".. This is a restructured text help text.")
    assert param.help_type == HelpType.RESTRUCTURED_TEXT

def test_detect_help_type_none():
    param = BaseParameter(name="param6", value=42, param_type=ParameterType.IntegerParameter, help=None)
    assert param.help_type == HelpType.SIMPLE

def test_is_path_valid(valid_file_path):
    param = BaseParameter(name="param7", value=valid_file_path, param_type=ParameterType.FileNameParameter)
    assert param.is_path("valid_path/to_file") == True

def test_is_path_invalid(valid_file_path):
    param = BaseParameter(name="param8", value=valid_file_path, param_type=ParameterType.FileNameParameter)
    assert param.is_path("invalid:path") == False

if __name__ == '__main__':
    pytest.main()