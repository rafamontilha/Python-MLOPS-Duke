fruit_list = ['apple', 'orange', 'grape', 'banana']

def test_first_fruit():
    result = fruit_list[0]
    # no PDB você digitaria:
    # (Pdb) p result       → 'apple'
    # (Pdb) p fruit_list   → ['apple', 'orange', 'grape', 'banana']
    assert result == 'mango'  # falha proposital