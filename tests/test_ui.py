from param123d.parameter_base import BaseParameter
from param123d.parameter_types import ParameterType
from param123d.parameters import BooleanParameter, IntegerParameter
from nicegui import ui

def main():
    a = BooleanParameter('a', True, help='A bool parameter')
    b = BooleanParameter('b', False, help='Another bool parameter')
    c = IntegerParameter('c', 42, min_value=10, max_value=100, step_value=10, default_value=50, unit='m', help='An **integer** parameter')   
    
    ui.label('Parameters')
    
    with ui.grid(columns='2fr 2fr auto'):	
        a.create_ui()
        b.create_ui()
        c.create_ui()
    
    ui.run()

if __name__ in {"__main__", "__mp_main__"}:
    main()