#ejemplo1
#este ejemplo se ve con pytest test_calculator.py
from calculator import square 

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0