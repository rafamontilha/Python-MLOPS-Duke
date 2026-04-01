# Write pytest test functions below to validate the following:
# 1. Check that is_even(4) returns True.
# 2. Check that add(2, 3) equals 5.
# 3. Check that multiply(3, 7) returns 21 with a detailed message if it fails.
# 4. Check that divide(10, 0) raises a ZeroDivisionError.
# 5. Check that 'grape' is in the fruit_list.

def is_even(num):
    return num % 2 == 0

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

fruit_list = ['apple', 'orange', 'grape', 'banana']

# Write your pytest test functions below. Name them as test_* following pytest convention.

def test_is_even():
    assert is_even(2)
# Write your code here

def test_add():
    assert add (2,2) == 4

def test_multiply():
    assert multiply(2,2) == 4
# Write your code here, use message: f"Expected 21, got {result}"

def test_divide_zero():
    assert divide(2,2) == 1
# Write your code here, use message: "Expected ZeroDivisionError when dividing by zero"

def test_grape_in_list():
    result = 'grape' in fruit_list
    assert result == True
# Write your code here