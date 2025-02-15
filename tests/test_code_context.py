import pytest
from param123d.code_context import CodeContext
from pathlib import Path

@pytest.fixture
def valid_file_path():
    return str(Path(__file__).parent / "test_file.py")

@pytest.fixture
def invalid_file_path():
    return str(Path(__file__).parent / "invalid_file.py")

@pytest.fixture
def code_context_data():
    return ["line1", "line2", "line3", "line4", "line5"]

def test_valid_code_context_initialization(valid_file_path, code_context_data):
    file_name = valid_file_path
    line_number = 5
    positions = (0, 5)
    
    context = CodeContext(file_name, line_number, positions, code_context_data)
    
    assert context.file_name == file_name
    assert context.line_number == line_number
    assert context.positions == positions
    assert context.code_context == code_context_data

def test_invalid_file_name(invalid_file_path, code_context_data):
    with pytest.raises(ValueError, match="Invalid file name"):
        CodeContext(invalid_file_path, 5, (0, 5), code_context_data)

def test_invalid_line_number(valid_file_path, code_context_data):
    with pytest.raises(ValueError, match="Invalid line number"):
        CodeContext(valid_file_path, 100, (0, 5), code_context_data)

def test_extract_code_context(valid_file_path, code_context_data):
    file_name = valid_file_path
    line_number = 5
    positions = (1, 3)
    
    context = CodeContext(file_name, line_number, positions, code_context_data)
    
    assert context.extract_code_context() == "line1\nline2\nline3\nline4\nline5"

def test_str_representation(valid_file_path, code_context_data):
    file_name = valid_file_path
    line_number = 5
    positions = (1, 3)
    
    context = CodeContext(file_name, line_number, positions, code_context_data)
    
    assert f'File: ' in str(context)
    assert f':L5:' in str(context)

def test_is_valid_file_name(valid_file_path, invalid_file_path, code_context_data):
    context = CodeContext(valid_file_path, 5, (0, 5), code_context_data)
    assert context.is_valid_file_name(valid_file_path) == True
    assert context.is_valid_file_name(invalid_file_path) == False

def test_is_valid_line_number(valid_file_path, code_context_data):
    context = CodeContext(valid_file_path, 4, (0, 5), code_context_data)
    assert context.is_valid_line_number(3) == True
    assert context.is_valid_line_number(100) == False
