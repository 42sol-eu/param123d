from param123d import ParameterGroup, Parameter

#%% [Parameters]
with ParameterGroup("MyGroup"):
    a = Parameter(default=42)
    b = Parameter(default="Hello")
    c = 10

#%% Another Section
some_other_code = 123