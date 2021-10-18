from pytest import *

from component_box import ComponentBox
from rotor import Rotor

def test_sinlge_rotor_i_position_a():
    cb = ComponentBox()
    r = cb.getRotor('I')
    assert r.rightToLeft(0) == 4

def test_sinlge_rotor_ii_position_a():
    cb = ComponentBox()
    r = cb.getRotor('II')
    assert r.rightToLeft(24) == 14

def test_three_rotors_i_positions_aaa():
    cb = ComponentBox()
    rotors = [cb.getRotor('I'), cb.getRotor('I'), cb.getRotor('I')]
    input = 0
    input = rotors[0].rightToLeft(input)
    input = rotors[1].rightToLeft(input)
    result = rotors[2].rightToLeft(input)
    assert result == (ord('T') - 65)

def test_default_position_rotor_i():
    cb = ComponentBox()
    rotor = cb.getRotor('I')
    assert rotor.getPosition() == 'A'

def test_rotor_i_rotate_one_position():
    cb = ComponentBox()
    rotor = cb.getRotor('I')
    rotor.rotate()
    assert rotor.getPosition() == 'B'

def test_rotor_i_rotate_five_positions():
    cb = ComponentBox()
    rotor = cb.getRotor('I')
    for i in range(5):
        rotor.rotate()
    assert rotor.getPosition() == 'F'

def test_rotor_i_full_rotation():
    cb = ComponentBox()
    rotor = cb.getRotor('I')
    for i in range(26):
        rotor.rotate()
    assert rotor.getPosition() == 'A'

def test_set_rotor_position():
    cb = ComponentBox()
    rotor = cb.getRotor('I')
    rotor.setPosition('J')
    assert rotor.getPosition() == 'J'

def test_rotor_i_hit_turnover():
    cb = ComponentBox()
    rotor = cb.getRotor('I')
    rotor.setPosition('Q')
    assert rotor.inTurnoverPosition() == True
    rotor.rotate()
    assert rotor.hasTurnedover() == True

def test_rotor_i_doesnt_hit_turnover():
    cb = ComponentBox()
    rotor = cb.getRotor('I')
    rotor.setPosition('R')
    assert rotor.inTurnoverPosition() == False
    rotor.rotate()
    assert rotor.hasTurnedover() == False

def test_rotor_vi_hit_turnovers():
    cb = ComponentBox()
    rotor = cb.getRotor('VI')
    rotor.setPosition('Z')
    assert rotor.inTurnoverPosition() == True
    rotor.rotate()
    assert rotor.hasTurnedover() == True
    rotor.setPosition('M')
    assert rotor.inTurnoverPosition() == True
    rotor.rotate()
    assert rotor.hasTurnedover() == True