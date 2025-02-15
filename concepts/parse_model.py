from redbaron import RedBaron

code = """
#%% [Parameters]
with ParameterGroup("MyGroup"):
    my_param = IntegerParameter(default=42)
    another_param = StringParameter(default="Hello")
    unrelated_var = 10

#%% Another Section
some_other_code = 123
"""

# Parse code
red = RedBaron(code)

# Step 1: Locate the parameters section
lines = code.split("\n")
inside_section = False
section_code = []
start_line = None

for i, line in enumerate(lines):
    if line.strip().startswith("#%% [Parameters]"):
        inside_section = True
        start_line = i + 1  # 1-based line number
        continue
    elif line.strip().startswith("#%%") and inside_section:
        break  # Stop at the next #%%
    
    if inside_section:
        section_code.append(line)

# Parse section separately
section_code = "\n".join(section_code)
section = RedBaron(section_code)

# Step 2: Find `with` blocks containing `ParameterGroup`
for with_block in section.find_all("with"):
    if "ParameterGroup" in with_block.dumps():  # Check for ParameterGroup presence
        with_name = with_block.value[0].dumps()  # Extract name
        with_line = start_line + with_block.absolute_bounding_box.top_left.line - 1  # Adjust for section offset

        print(f"Found ParameterGroup '{with_name}' at line {with_line}")

        # Step 3: Extract all assignments inside `with`
        for node in with_block.value.find_all("assign"):
            var_name = node.target.dumps()
            value = node.value.dumps()
            print(f"  Assignment: {var_name} = {value}")

        # Step 4: Extract all `Parameter(...)` definitions
        for call in with_block.find_all("call"):
            if "Parameter" in call.dumps():  # Check for Parameter function calls
                print(f"  Parameter definition: {call.dumps()}")
