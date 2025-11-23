from myproject import myModule


def test_top_n():
    """
    Make sure top_n works correctly
    """
    
    assert myModule.top_n([8,3,32,7,4], 3) == [8,7,4], 'Incorrect'
    assert myModule.top_n([10,12,3,9,4,2,11,15,8], 5) == [15,12,11,10,9], 'Incorrect'
    assert myModule.top_n([9,3,7,6,4], 2) == [9,7,], 'Incorrect'