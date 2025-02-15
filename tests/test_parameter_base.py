import pytest
from pathlib import Path
from param123d.parameter_base import BaseParameter, RangeParameter, CalculationParameter
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

    param = BaseParameter("test_angle", 45, ParameterType.AngleParameter)
    assert param.is_valid_type(45) == True
    assert param.is_valid_type(45.0) == True
    assert param.is_valid_type("45") == False

    param = BaseParameter("test_length", 10, ParameterType.LengthParameter)
    assert param.is_valid_type(10) == True
    assert param.is_valid_type(-10) == False

    param = BaseParameter("test_area", 100, ParameterType.AreaParameter)
    assert param.is_valid_type(100) == True
    assert param.is_valid_type(-100) == False

    param = BaseParameter("test_volume", 1000, ParameterType.VolumeParameter)
    assert param.is_valid_type(1000) == True
    assert param.is_valid_type(-1000) == False

    param = BaseParameter("test_mass", 50, ParameterType.MassParameter)
    assert param.is_valid_type(50) == True
    assert param.is_valid_type(-50) == False

    param = BaseParameter("test_time", 60, ParameterType.TimeParameter)
    assert param.is_valid_type(60) == True
    assert param.is_valid_type(-60) == False

    param = BaseParameter("test_speed", 30, ParameterType.SpeedParameter)
    assert param.is_valid_type(30) == True
    assert param.is_valid_type(-30) == True

    param = BaseParameter("test_acceleration", 9.8, ParameterType.AccelerationParameter)
    assert param.is_valid_type(9.8) == True
    assert param.is_valid_type(-9.8) == True

    param = BaseParameter("test_force", 100, ParameterType.ForceParameter)
    assert param.is_valid_type(100) == True
    assert param.is_valid_type(-100) == True

    param = BaseParameter("test_torque", 200, ParameterType.TorqueParameter)
    assert param.is_valid_type(200) == True
    assert param.is_valid_type(-200) == True

    param = BaseParameter("test_temperature", 37, ParameterType.TemperatureParameter)
    assert param.is_valid_type(37) == True
    assert param.is_valid_type(3.7) == True
    
    assert param.is_valid_type(-37) == True
    assert param.is_valid_type(-3.7) == True

    assert param.is_valid_type('abc') == False


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
    assert param.is_valid_type(invalid_file_path) == False
    assert param.is_valid_type(valid_file_path) == False
    assert param.is_valid_type(1) == False

    param = BaseParameter("test_file", valid_file_path, ParameterType.FileParameter)
    assert param.is_valid_type(valid_file_path) == True 
    assert param.is_valid_type(invalid_file_path) == False

    param = BaseParameter("test_path", valid_file_path.parent, ParameterType.PathParameter)
    assert param.is_valid_type(valid_file_path.parent) == True 

def test_range_parameter_is_valid_type():
    param = RangeParameter("test_range", 10, ParameterType.IntegerParameter, "m", min_value=0, max_value=20)
    assert param.is_valid_type(10) == True
    assert param.is_valid_type(30.0) == False

def test_calculation_parameter_is_valid_type():
    param = CalculationParameter("test_calc", 10, ParameterType.IntegerParameter, "m", calc="5 + 5")
    assert param.is_valid_type(10) == True
    assert param.is_valid_type("10") == False