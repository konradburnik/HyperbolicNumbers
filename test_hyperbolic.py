from hyperbolic import *
import pytest

def test_hyperbolic_add():
    assert HyperbolicNumber(1, 2) + HyperbolicNumber(3, 4) == HyperbolicNumber(4, 6), "Testing add"

def test_scaling():
    assert 2 * HyperbolicNumber(1,2) == HyperbolicNumber(2,4)
    assert -1 * HyperbolicNumber(1,2) == HyperbolicNumber(-1,-2)

def test_mag():
    assert mag(HyperbolicNumber(1, 0)) == 1.0
