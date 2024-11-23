def next_ten_numbers(num):
    """Generates the next 10 numbers from the given number as a comma-delimited string.

    Args:
        num: The starting number.

    Returns:
        A string containing the next 10 numbers separated by commas.
    """
    return ','.join(str(num + i) for i in range (1, 11))
def test_should_return_next_ten_numbers_as_comma_delimited_string():
    assert next_ten_numbers(5) == "6,7,8,9,10,11,12,13,14,15"
def test_should_return_comma_delimited_string_from_list():
    assert list_to_comma_delimited_string(["apple", "banana", "cherry"]) == "apple,banana,cherry"