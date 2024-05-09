def is_integer(value):
    """
    Checks if a value is an integer.

    Args:
        value (any): The value to be checked.

    Returns:
        bool: True if the value is an integer, False otherwise.
    """
    return isinstance(value, int) and not isinstance(value, bool)
