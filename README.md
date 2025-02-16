# param123d - Parametric Models 

## Concepts 

Every parameter has:

- A group it belongs to
- A name it is referenced with
- A value it holds 
- A type it represents
- A help documentation (may be markdown or restructured text)

Parameter can be grouped in:

- `BaseParameter`: a simple value like a `boolean`, a `string` or a `color`.
- `ChoiceParameter`: a selection of values `choices` that can map to a specific value.
- `RangeParameter`: defines a range via `min` and `max` and an additional `step` and an optional `unit` element.
- `CalculationParameter`: introduces a `calc` element in the constructor, that can hold a Python expression an optional `unit` element.

## UI Element Mapping

`number` is either an `int` or a `float` value. 

### `ParameterGroup` 

| nicegui element | parameter type | notes |
|-----------------|----------------|-------|
| `ui.expansion`  |                |       |
| `ui.badge`      |                |       |


### `BaseParameter`

| nicegui element  | parameter type | notes |
|------------------|----------------|-------|
| `ui.switch`      | `boolean`      |       |
| `ui.checkbox`    | `boolean`      |       |
| `ui.input`       | `string`       |       |
| `ui.number`      | `number`       |       |
| `ui.color_input` | `color`        |       |
| `ui.color_picker`| `color`        |       |

### `ChoiceParameter`

| nicegui element | parameter type | notes |
|-----------------|----------------|-------|
| `ui.toggle`     |                |       |
| `ui.radio`      |                |       |
| `ui.select`     |                |       |
| `ui.icon`       | `icon`         |       |

> [!Note]
> `ui.select` can keep a `list` and a `dict`. The `dict` can be used to map visible values to internal values (e.g. readable names to numbers, color names to color values)

> [!Note]
> Use this also for Fonts, Axis, Planes

### `RangeParameter`

| nicegui element | parameter type | notes |
|-----------------|----------------|-------|
| `ui.input`      | `number`       |       |
| `ui.number`     | `number`       |       |
| `ui.slider`     | `number`       |       |
| `ui.range`      | 2*`number`     |       |
| `ui.knob`       | `number`       |       |
|                 |                |       |

> [!Note]
> Use validation `dict` to check for ranges `{'message': lambda value: expression_OK}`

> [!Note]
> Check if min,max and step should be put into a `NamedTuple`

### `CalculationParameter`

| nicegui element | parameter type | notes |
|-----------------|----------------|-------|
| `ui.input`      | `calc`         |       |
| `ui.textarea`   | `calc`         |       |

> [!Note]
> Calculation should have an additional element to show the calculated value.

## Advices

Using the `abstract syntax tree` to analyze the code for `ParameterGroup` and `{Type}Parameter`.

It is advisable to:
    1. Use `with` block with `ParameterGroup()` in the main context.
    2. Use the `with ParameterGroup() as {name}:` to reference the parameters later `{name}.{parameter_name}`, like `pars.width` 
    3. Use `{Type}Parameter()` in the with-block
    4. Use assignments for parameters if you need to reference them in later calculations.
    5. Use mainly parameter definitions in the `with` block with the `ParameterGroup` definition. (`ast` should work mostly fine with other code, but it is not recommendet to mix your parameters with functional code)
  6. Use the best fitting type for you parameter, selectig more specific parameters where ever possible.
  7. Be aware of the `calc={expression}` parameter and the restrictions, that you are allowed to use inside the `calc`-expression.
  8. Be aware of the possible usage of global variables to calcualate you parameter values.
  9. Parameters can use validator functions
  10. Be aware of parameter-sets that are stored as `yaml` files in the model folder. You can store the parameter-sets
  11. Avoid additional logic or statements in the `with` block or around the `{Type}Parameter` definitions like `if` or `for` because the parser will not be able to register this statements logic or show it in the user interface.


## Setup

```
# 1a via pipx 
python -m pip install pipx 
pipx install poetry
which poetry

# 1b via scoop
scoop install poetry
which poetry

# 2
poetry config virtualenvs.in-project true
poetry lock
poetry install 

# 3
eval $(poetry env activate)

## Inital setup ...

poetry add --dev pytest