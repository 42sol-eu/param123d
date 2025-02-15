from param123d import ParameterGroup, BaseParameter

#%% [Parameters]
with ParameterGroup("MyGroup"):
    a = BaseParameter(default=42)
    b = BaseParameter(default="Hello")
    c = 10

#%% Another Section
some_other_code = 123