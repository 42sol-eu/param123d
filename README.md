# param123d - Parametric Models 

## Concepts 

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