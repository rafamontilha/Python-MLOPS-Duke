def calculate_average(num1, num2):
    return (num1 + num2) / 2

# Test function using pytest's parametrize
import pytest

@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (10, 20, 15),
        (20, 30, 25),
        (5, 5, 5)
    ])
def test_calculate_average(num1, num2, expected):
    assert (calculate_average(num1, num2) == expected), f"Average of {num1} and {num2} should be equal to {(num1 + num2) / 2}"