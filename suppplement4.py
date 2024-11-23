def next_ten_numbers(num):
    """Generates the next 10 numbers from the given number as a comma-delimited string.

    Args:
        num: The starting number.

    Returns:
        A string containing the next 10 numbers separated by commas.
    """
    return ','.join(str(num + i) for i in range (1, 11))

def list_to_comma_delimited_string(strings):
    """Converts a list of strings to a comma-delimited string.

    Args:
        strings: A list of strings.

    Returns:
        A single string where each element is separated by a comma.
    """
    return ','.join(strings)
def get_headers():
    return["Name", "Age", "Profession"]
def test_should_return_next_ten_numbers_as_comma_delimited_string():
    assert next_ten_numbers(5) == "6,7,8,9,10,11,12,13,14,15"
def test_should_return_comma_delimited_string_from_list():
    assert list_to_comma_delimited_string(["apple", "banana", "cherry"]) == "apple,banana,cherry"
def test_should_write_csv_file():
    """Tests the write_csv_file function."""
    write_csv_file("test.csv")

    with open("test.csv", mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        # Test headers
        assert rows[0] == ["Name", "Age", "Profession"], "Headers do not match."

        # Test data
        assert rows[1:] == [
            ["Chance", "21", "Engineer"],
            ["Bob", "30", "Designer"],
            ["Charlie", "22", "Data Scientist"]
        ], "Data rows do not match."