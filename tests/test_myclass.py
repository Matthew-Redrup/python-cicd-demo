import pytest

from python_cicd_demo.myclass import MyClass


class TestMyClass:
    def test_my_function_with_valid_input(self):
        obj = MyClass()
        assert obj.my_function("World") == "Hello World", "Incorrect greeting generated"

    def test_my_function_with_non_string_input(self):
        obj = MyClass()
        with pytest.raises(ValueError) as excinfo:
            obj.my_function(None)
        assert (
            str(excinfo.value) == "input_string must be a string"
        ), "ValueError not raised as expected for non-string input"

        with pytest.raises(ValueError) as excinfo:
            obj.my_function(123)  # Testing with an integer
        assert (
            str(excinfo.value) == "input_string must be a string"
        ), "ValueError not raised as expected for non-string input"
