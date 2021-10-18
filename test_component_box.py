from pytest import *

from component_box import ComponentBox

def test_generated_components():
    cb = ComponentBox()

def test_get_rotor():
    cb = ComponentBox()
    rotor = cb.getRotor('VI')
    assert rotor.getName() == 'VI'

def test_get_rotor_wrong_name():
    cb = ComponentBox()
    assert cb.getRotor('X') == None

def test_get_reflector():
    cb = ComponentBox()
    reflector = cb.getReflector('C')
    assert reflector.getName() == 'C'

def test_get_reflector_wrong_name():
    cb = ComponentBox()
    assert cb.getReflector('I') == None

def test_list_rotors():
    target = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
    cb = ComponentBox()
    assert cb.listRotors() == target

def test_list_reflectors():
    target = ['A', 'B', 'C']
    cb = ComponentBox()
    assert cb.listReflectors() == target