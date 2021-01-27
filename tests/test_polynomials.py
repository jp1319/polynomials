from polynomials import Polynomial

def test_print():
    p = Polynomial((1, 3, 0, 5, 1))
    q = Polynomial((0,))
    assert str(p) == "x^4 + 5x^3 + 3x + 1" and str(q) == "0"

def test_equality():
    assert Polynomial((0, 1)) == Polynomial((0,1))
