from scr.complex_numbers import _complex
from math import isclose

def test_add():
    a = _complex(1,2)
    b = _complex(3,4)
    add_c = a+b
    assert isclose(add_c.real, 4) and isclose(add_c.im, 6), 'Addition failed!'
    
def test_sub():
    a = _complex(-1,2)
    b = _complex(4,-2)
    add_c = a-b
    assert isclose(add_c.real, -5) and isclose(add_c.im, 4), 'Subtraction failed!'

def test_mul():
    a = _complex(10,3)
    b = _complex(4,6)
    add_c = a*b
    assert isclose(add_c.real, 22) and isclose(add_c.im, 72), 'Multiplication failed!'

def test_div():
    a = _complex(-1,-2)
    b = _complex(-2,2)
    add_c = a/b
    assert isclose(add_c.real, -0.25) and isclose(add_c.im, 0.75), 'Division failed!'
