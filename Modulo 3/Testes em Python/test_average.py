# test_average.py
def average(a, b):
    return (a + b) / 2

def test_average_positive():
    assert average(4, 6) == 5.0

def test_average_negative():
    assert average(-3, -1) == -2.0

def test_average_zero():
    assert average(0, 0) == 0.0
