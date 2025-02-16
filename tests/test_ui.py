from param123d.parameter_base import BaseParameter, RangeParameter, CalculationParameter
from param123d.parameter_types import ParameterType
from param123d.parameters import BooleanParameter, IntegerParameter, FloatParameter, StringParameter, ChoiceParameter
from nicegui import ui

def main():
    # Core Types
    a = BooleanParameter('a', True, help='A bool parameter')
    b = BooleanParameter('b', False, help='Another bool parameter')
    c = IntegerParameter('c', 42, min_value=10, max_value=100, step_value=10, default_value=50, unit='m', help='An **integer** parameter')   
    d = FloatParameter('d', 3.14, min_value=0.0, max_value=10.0, step_value=0.1, default_value=1.0, unit='m', help='A float parameter')
    e = StringParameter('e', 'String Text', help='A string parameter')
    
    # Base classes types 
    f = BaseParameter('f', 'Base Test', ParameterType.StringParameter, help='A string parameter')
    # TODO: choice parameter
    g = ChoiceParameter('g', ['A', 'B', 'C'], 'B', help='A choice parameter with list')
    h = ChoiceParameter('h', {15: '15 mm', 18: '18 mm', 22: '22 mm'}, 'B', help='A choice parameter with dict')
    i = RangeParameter('h', 20.0, ParameterType.RangeParameter,  min_value=10.0, max_value=100.0, step_value=10.0, default_value=10.0, unit='mm', help='A range parameter')
    j = CalculationParameter('i', c + 10, ParameterType.RangeParameter, help='TODO: incomplete calculation parameter', unit='mm')
    
    # More types
    
    views = [a, b, c, d, e, f, g, h, i, j]
    
    with ui.row():
        # ui.icon('paint_brush').classes('text-5xl').style(add='color: #ff0000')
        ui.space()
        ui.label('Parameters').classes('text-2xl')
        
    with ui.grid(columns='2fr 2fr 4fr'):	
        for view in views:
            view.create_ui()
    
    with ui.row():
        ui.button('Check')
        ui.button('Apply')
    
    ui.run()

if __name__ in {"__main__", "__mp_main__"}:
    main()