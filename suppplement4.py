import csv
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
def get_data():
     """Generates a list of data rows.

    Returns:
        A list of lists, where each inner list represents a row of data.
    """
     return [
        ["Chance", 21, "Engineer"],  # Updated row
        ["Bob", 30, "Designer"],
        ["Charlie", 22, "Data Scientist"]
    ]


def get_headers():
    """Generates the headers for the CSV file.

    Returns:
        A list representing the column headers.
    """
    return ["Name", "Age", "Profession"]


def write_csv_file(filename):
    """Writes the headers and data to a CSV file.

    Args:
        filename: The name of the CSV file to create.
    """
    headers = get_headers()
    data = get_data()

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)  # Write headers
        writer.writerows(data)  # Write data rows


def test_should_return_next_ten_numbers_as_comma_delimited_string():
    assert next_ten_numbers(5) == "6,7,8,9,10,11,12,13,14,15"
def test_should_return_comma_delimited_string_from_list():
    assert list_to_comma_delimited_string(["apple", "banana", "cherry"]) == "apple,banana,cherry"

def test_should_write_csv_file():
    """Tests the write_csv_file function."""
    filename = "test.csv"
    write_csv_file(filename)

    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        # Test headers
        assert rows[0] == ["Name", "Age", "Profession"], "Headers do not match."

        # Test data
        assert rows[1:] == [
            ["Chance", "21", "Engineer"],  # Updated test case
            ["Bob", "30", "Designer"],
            ["Charlie", "22", "Data Scientist"]
        ], "Data rows do not match."
