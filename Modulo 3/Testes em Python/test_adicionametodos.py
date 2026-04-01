fruit_list = ['apple', 'orange', 'grape', 'banana']

class TestFruitList:
    
    def test_grape_in_list(self):
        assert 'grape' in fruit_list, f"Expected 'grape' to be in list"
    
    def test_list_length(self):
        result = len(fruit_list)
        assert result == 4, f"Expected 4, got {result}"
    
    def test_first_fruit(self):
        result = fruit_list[0]
        assert result == 'apple', f"Expected 'apple', got {result}"