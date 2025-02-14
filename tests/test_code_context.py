import pytest
from param123d.code_context import CodeContext

def test_valid_code_context_initialization():
    file_name = "test_file.py"
    line_number = 10
    positions = (0, 5)
    code_context = ["line1", "line2", "line3", "line4", "line5"]
    
    context = CodeContext(file_name, line_number, positions, code_context)
    
    assert context.file_name == file_name
    assert context.line_number == line_number
    assert context.positions == positions
    assert context.code_context == code_context

def test_invalid_file_name():
    with pytest.raises(ValueError, match="Invalid file name: invalid_file.py"):
        CodeContext("invalid_file.py", 10, (0, 5), ["line1", "line2", "line3", "line4", "line5"])

def test_invalid_line_number():
    with pytest.raises(ValueError, match="Invalid line number: 100 file test_file.py has only 5 lines"):
        CodeContext("test_file.py", 100, (0, 5), ["line1", "line2", "line3", "line4", "line5"])

def test_extract_code_context():
    file_name = "test_file.py"
    line_number = 10
    positions = (1, 3)
    code_context = ["line1", "line2", "line3", "line4", "line5"]
    
    context = CodeContext(file_name, line_number, positions, code_context)
    
    assert context.extract_code_context() == ["line2", "line3"]

def test_str_representation():
    file_name = "test_file.py"
    line_number = 10
    positions = (1, 3)
    code_context = ["line1", "line2", "line3", "line4", "line5"]
    
    context = CodeContext(file_name, line_number, positions, code_context)
    
    assert str(context) == "File: test_file.py:L10: ['line2', 'line3']"

def test_is_valid_file_name():
    context = CodeContext("test_file.py", 10, (0, 5), ["line1", "line2", "line3", "line4", "line5"])
    assert context.is_valid_file_name("test_file.py") == True
    assert context.is_valid_file_name("invalid_file.py") == False

def test_is_valid_line_number():
    context = CodeContext("test_file.py", 4, (0, 5), ["line5"])
    assert context.is_valid_line_number(3) == True
    assert context.is_valid_line_number(100) == False