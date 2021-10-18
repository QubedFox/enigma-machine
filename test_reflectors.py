from pytest import *

from component_box import ComponentBox
from reflector import Reflector

def test_reflector_a():
    cb = ComponentBox()
    r: Reflector = cb.getReflector('A')
    assert r.reflect(7) == 23

def test_reflector_b():
    cb = ComponentBox()
    r: Reflector = cb.getReflector('B')
    assert r.reflect(7) == 3