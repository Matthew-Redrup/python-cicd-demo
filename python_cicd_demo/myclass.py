"""
A simple python script to demonstrate CI/CD
"""

__version__ = "0.1.0"


class MyClass:
    """A simple example class"""

    i = 12345

    def my_function(self, input_string: str) -> str:
        """
        Return a greeting message with the given input string.

        :param input_string: A string input.
        :type input_string: str
        :raises ValueError: If input_string is not a string.
        :return: A greeting message.
        :rtype: str
        """
        if not isinstance(input_string, str):
            raise ValueError("input_string must be a string")
        return f"Hello {input_string}"
