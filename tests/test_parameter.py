"""
This module contains the tests for the Parameter from `parameter_base` module.
"""

import pytest
from param123d.parameter_base import BaseParameter
from param123d.parameter_types import ParameterType

def test_valid_parameter_initialization():
    param = BaseParameter(name="valid_name", value=10.0, param_type=ParameterType.FloatParameter)
    assert param.name == "valid_name"
    assert param.value == 10.0
    assert param.param_type == ParameterType.FloatParameter

def test_invalid_parameter_name():
    with pytest.raises(ValueError, match="Parameter name 'invalid name' is not a valid Python identifier."):
        BaseParameter(name="invalid name", value=10.0, param_type=ParameterType.FloatParameter)

def test_invalid_parameter_value_type():
    with pytest.raises(ValueError, match="Parameter value 'invalid' is not a valid value for type 'ParameterType.FloatParameter'."):
        BaseParameter(name="valid_name", value="invalid", param_type=ParameterType.FloatParameter)
