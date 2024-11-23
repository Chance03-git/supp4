def next_ten_numbers(num):
    return ','.join(str(num + i) for i in range (1, 11))
def test_should_return_next_ten_numbers_as_comma_delimited_string():
    assert next_ten_numbers(5) == "6,7,8,9,10,11,12,13,14,15"