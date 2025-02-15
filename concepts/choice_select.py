from nicegui import ui

with ui.row():
    select1 = ui.select([1, 2, 3], value=1)
    value1 = ui.number(select1.value)
    value1.bind_value_from(select1, 'value')
    
with ui.row():
    select2 = ui.select({1: 'One', 2: 'Two', 3: 'Three'})
    value2 = ui.number(select2.value)
    value2.bind_value_from(select2, 'value')
ui.run()