"""
A code context object to capture file name, line number, and code context.
"""

from dataclasses import dataclass
from typing import List, Optional, Tuple
from pathlib import Path


# TODO: is this really necessary (maybe yes if `ast` is used). But `RedBaron` can manipulate the values directly.

@dataclass
class CodeContext:
    file_name: Optional[str] = None
    line_number: Optional[int] = None
    positions: Optional[Tuple[int, int]] = None
    code_context: Optional[List[str]] = None
    
    def __init__(self, file_name: str, line_number: int, positions: Tuple[int, int], code_context: List[str]):
        
        if not self.is_valid_file_name(file_name):
            raise ValueError(f"Invalid file name: {file_name}")
        
        self.file_name = file_name
        
        if not self.is_valid_line_number(line_number):
            raise ValueError(f"Invalid line number: {line_number} file {file_name} has only {self.line_counter} lines")
        
        self.line_number = line_number
        
        # TODO: Check if positions are valid 
        self.positions = positions        
        # TODO: code_context is valid
        self.code_context = code_context
    
    @classmethod
    def from_frame_info(cls, frame_info):
        
        return CodeContext(frame_info.filename, frame_info.lineno, frame_info.positions, frame_info.code_context)
    
    def __str__(self) -> str:
        return f"File: {self.file_name}:L{self.line_number}: {self.extract_code_context()}"
    
    def is_valid_file_name(self, value : str) -> bool:
        print(f'>>>> {__file__}')
        return isinstance(value,str) and Path(value).exists()
    
    def is_valid_line_number(self, value : int) -> bool:
        value_type = isinstance(value,int)
        
        with open(self.file_name) as f:
            self.line_counter = sum(1 for _ in f)
            
        return value_type and value <= self.line_counter
