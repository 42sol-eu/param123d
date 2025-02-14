"""
This module contains the tests for the Parameter from `parameter_base` module.
"""

import pytest
from param123d.parameter_base import Parameter
from param123d.parameter_types import ParameterType

def test_valid_parameter_initialization():
    param = Parameter(name="valid_name", value=10.0, param_type=ParameterType.FloatParameter, unit="m")
    assert param.name == "valid_name"
    assert param.value == 10.0
    assert param.unit == "m"
    assert param.param_type == ParameterType.FloatParameter

def test_invalid_parameter_name():
    with pytest.raises(ValueError, match="Parameter name 'invalid name' is not a valid Python identifier."):
        Parameter(name="invalid name", value=10.0, param_type=ParameterType.FloatParameter, unit="m")

def test_invalid_parameter_value_type():
    with pytest.raises(ValueError, match="Parameter value 'invalid' is not a valid value for type 'ParameterType.FloatParameter'."):
        Parameter(name="valid_name", value="invalid", param_type=ParameterType.FloatParameter, unit="m")

def test_invalid_min_value_type():
    with pytest.raises(ValueError, match="Parameter min_value 'invalid' is not a valid value for type '<class 'float'>' determined by the given value."):
        Parameter(name="valid_name", value=10.0, param_type=ParameterType.FloatParameter, unit="m", min_value="invalid")

def test_invalid_max_value_type():
    with pytest.raises(ValueError, match="Parameter max_value 'invalid' is not a valid value for type '<class 'float'>' determined by the given value."):
        Parameter(name="valid_name", value=10.0, param_type=ParameterType.FloatParameter, unit="m", max_value="invalid")

def test_min_value_greater_than_max_value():
    with pytest.raises(ValueError, match="Parameter min_value '20.0' is greater than max_value '10.0'."):
        Parameter(name="valid_name", value=10.0, param_type=ParameterType.FloatParameter, unit="m", min_value=20.0, max_value=10.0)

def test_invalid_step_value_type():
    with pytest.raises(ValueError, match="Parameter step_value 'invalid' is not a valid value for type '<class 'float'>' determined by the given value."):
        Parameter(name="valid_name", value=10.0, param_type=ParameterType.FloatParameter, unit="m", step_value="invalid")

def test_step_value_greater_than_range():
    with pytest.raises(ValueError, match="Parameter step_value '15.0' is greater than the range of min_value '5.0' and max_value '10.0'."):
        Parameter(name="valid_name", value=10.0, param_type=ParameterType.FloatParameter, unit="m", min_value=5.0, max_value=10.0, step_value=15.0)

def test_invalid_default_value_type():
    with pytest.raises(ValueError, match="Parameter default_value 'invalid' is not a valid value for type '<class 'float'>' determined by the given value."):
        Parameter(name="valid_name", value=10.0, param_type=ParameterType.FloatParameter, unit="m", default_value="invalid")

def test_default_value_greater_than_max_value():
    with pytest.raises(ValueError, match="Parameter default_value '15.0' is greater than max_value '10.0'."):
        Parameter(name="valid_name", value=10.0, param_type=ParameterType.FloatParameter, unit="m", max_value=10.0, default_value=15.0)

def test_default_value_smaller_than_min_value():
    with pytest.raises(ValueError, match="Parameter default_value '5.0' is smaller than min_value '10.0'."):
        Parameter(name="valid_name", value=10.0, param_type=ParameterType.FloatParameter, unit="m", min_value=10.0, default_value=5.0)