"""

Parameter groups for usage in `with` blocks.
    
"""


class ParameterGroup:
    """A context manager to capture file name and line number for the with block."""

    def __init__(self):
        self._context = None

    def __enter__(self):
        """Capture file and line number of the calling script when entering the context."""
        stack = inspect.stack()
        stack_size = len(stack)
        caller_frame = None

        for i in range(stack_size):
            print(stack[i].code_context)
            for context in stack[i].code_context:
                if context.find('ParameterGroup')>= 0:
                    caller_frame = stack[i]
                    break
                
        if caller_frame:
            self._context = CodeContext(caller_frame)
            logging.info(f"Entered 'with' block in file: {self.context}")
        
        else:
            logging.error("Stack frame not found")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Exit the context."""
        if self.context:
            logging.info(f"Exiting 'with' block in context {self.context}")

