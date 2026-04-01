# Plain assert checking values  
def test_floats():
    result = 1.2 + 1.3
    assert result == 2.5
    
# Test class with setup/teardown    
class TestDivide:

    def setup(self):
        self.calculator = Calculator()

    def teardown(self):
        del self.calculator

    def test_divide_two_numbers(self):
        assert self.calculator.divide(10, 5) == 2 

# Parametrized test function 
@pytest.mark.parametrize("num", [1, 5, 10])
def test_squared(num):
    assert num * num == square(num)