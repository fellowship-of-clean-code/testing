from my_project.sorting import sort_list

def test_sorting_inverted_list():
    
    data = [5, 4, 3, 2, 1]
    should_be_sorted = sort_list(data)
    
    assert should_be_sorted == [1, 2, 3, 4, 5]

