import unittest

class TestesConvencoes(unittest.TestCase):

    def test_assertion(self):
        self.assertEqual("some string", "some other string")

unittest.main(argv=[''], verbosity=2, exit=False)

import unittest

class TestesConvencoes2(unittest.TestCase):
    def test_assertion(self):
        self.assertNotAlmostEqual(2, 2)
    
unittest.main(argv=[''], verbosity=2, exit=False)

assert "this string is long" == "this string is Long", "this thing failed"

def test_my_function():
    assert 1 == 1

