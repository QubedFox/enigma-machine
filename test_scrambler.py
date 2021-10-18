from pytest import *

from scrambler import Scrambler
from component_box import ComponentBox
from plugboard import Plugboard

def test_scrambler_no_plugs_rotors_I_positions_aaa_reflector_a_no_rotation():
    cb = ComponentBox()
    s = Scrambler()
    pb = Plugboard()
    s.setRotor('fast', cb.getRotor('I'))
    s.setRotor('middle', cb.getRotor('I'))
    s.setRotor('slow', cb.getRotor('I'))
    s.setReflector(cb.getReflector('A'))
    input = pb.translate('A')
    input = s.scrambleLetter(input)
    input = pb.translate(input)
    assert input == 'S'

def test_scrambler_default_positions():
    cb = ComponentBox()
    s = Scrambler()
    s.setRotor('fast', cb.getRotor('I'))
    s.setRotor('middle', cb.getRotor('I'))
    s.setRotor('slow', cb.getRotor('I'))
    assert s.getRotorPositions() == 'A-A-A'

def test_scrambler_rotate_positions_rotors_i_ii_iii():
    cb = ComponentBox()
    s = Scrambler()
    s.setRotor('fast', cb.getRotor('I'))
    s.setRotor('middle', cb.getRotor('II'))
    s.setRotor('slow', cb.getRotor('III'))
    assert s.getRotorPositions() == 'A-A-A'
    s.rotateRotors()
    assert s.getRotorPositions() == 'A-A-B'

def test_scrambler_rotate_positions_rotors_i():
    cb = ComponentBox()
    s = Scrambler()
    s.setRotor('fast', cb.getRotor('I'))
    s.setRotor('middle', cb.getRotor('I'))
    s.setRotor('slow', cb.getRotor('I'))
    assert s.getRotorPositions() == 'A-A-A'
    s.rotateRotors()
    assert s.getRotorPositions() == 'A-A-B'

def test_scrambler_turnover_rotors():
    cb = ComponentBox()
    s = Scrambler()
    s.setRotor('fast', cb.getRotor('I'))
    s.setRotor('middle', cb.getRotor('I'))
    s.setRotor('slow', cb.getRotor('I'))
    s.setRotorPosition('fast', 'Q')
    assert s.getRotorPositions() == 'A-A-Q'
    s.rotateRotors()
    assert s.getRotorPositions() == 'A-B-R'

def test_scrambler_double_turnover():
    cb = ComponentBox()
    s = Scrambler()
    s.setRotor('fast', cb.getRotor('I'))
    s.setRotor('middle', cb.getRotor('I'))
    s.setRotor('slow', cb.getRotor('I'))
    s.setRotorPosition('fast', 'Q')
    s.setRotorPosition('middle', 'P')
    assert s.getRotorPositions() == 'A-P-Q'
    s.rotateRotors()
    assert s.getRotorPositions() == 'A-Q-R'
    s.rotateRotors()
    assert s.getRotorPositions() == 'B-R-S'

def test_scrambler_set_to_start_position():
    cb = ComponentBox()
    s = Scrambler()
    s.setRotor('fast', cb.getRotor('I'))
    s.setRotor('middle', cb.getRotor('I'))
    s.setRotor('slow', cb.getRotor('I'))
    s.setRotorPosition('fast', 'Q')
    s.setRotorPosition('middle', 'P')
    s.setRotorPosition('slow', 'T')