from nicegui import ui

last_RGBA = '#FF0000FF'
last_red = 255
last_green = 0
last_blue = 0
last_alpha = 255
new_alpha = 0

def update_rgba():
    RGBA.set_value(f"#{red.value:02x}{green.value:02x}{blue.value:02x}{alpha.value:02x}")
    color.set_value(RGBA.value)
    update_knob_colors()

def update_knob_colors():
    red.style(f'color: "#{red.value:02x}0000";')
    green.style(f'color: "#00{green.value:02x}00"')
    blue.style(f'color: "#0000{blue.value:02x}"')
    alpha.style(f'color: "#{alpha.value:02x}{alpha.value:02x}{alpha.value:02x}"')

def update_knobs():
    new_red = int(RGBA.value[1:3], 16)
    new_green = int(RGBA.value[3:5], 16)
    new_blue = int(RGBA.value[5:7], 16)
    if len(RGBA.value) > 8:
        new_alpha = int(RGBA.value[7:9], 16)
    else:
        pass
        
    red.set_value(new_red)
    green.set_value(new_green)
    blue.set_value(new_blue)
    alpha.set_value(new_alpha)
    
    global last_red, last_green, last_blue, last_RGBA
    last_red = new_red
    last_green = new_green
    last_blue = new_blue
    last_alpha = new_alpha
    last_RGBA = RGBA.value

    update_knob_colors()

def update_both():
    RGBA.set_value(color.value)
    update_knobs()

with ui.expansion(caption='Color Picker Experiment', icon="paint_brush").classes('w-50'):
    with ui.row():
        RGBA = ui.input('RGBA', on_change=update_knobs)
        
        # color = ui.color_input(on_change=update_both)
        # color = ui.color_picker(on_pick=update_both)

        color = ui.color_input(label='Color', value='#00000000',
                    on_change=update_both)

    with ui.row():
        red   = ui.knob(0, color="red", track_color="black", min=0, max=255, step=1, show_value=True, on_change=update_rgba)
        green = ui.knob(10, color="green", track_color="black", min=0, max=255, step=1, show_value=True, on_change=update_rgba)
        blue  = ui.knob(0, color="blue", track_color="black", min=0, max=255, step=1, show_value=True, on_change=update_rgba)
        alpha = ui.knob(0, color="yellow", track_color="black", min=0, max=255, step=1, show_value=True, on_change=update_rgba)

ui.run()