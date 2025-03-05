from main import count_a_letter, INPUT_ERROR
import pytest

def test_input_is_not_letter():
    result = count_a_letter("hi", "1")
    assert result == None

def test_input_is_not_sentence():
    result = count_a_letter("", "a")
    assert result is None

def test_successfully_counts_letters():
    result = count_a_letter("hello world", "o")
    assert result == 2

def test_succesfully_counts_0_letters():
    result = count_a_letter("hello world", "a")
    assert result == 0
    

def test_value_error():
    non_string_input = 1
    with pytest.raises(ValueError) as received_error:
      count_a_letter("hello world", non_string_input)
    expected = f"({non_string_input}, '{INPUT_ERROR}')"
    assert str(received_error.value) == expected
