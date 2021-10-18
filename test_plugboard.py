from pytest import *

from plugboard import Plugboard

def test_plugboard_input_string():
    pb = Plugboard()
    assert pb.translate('A') == 0

def test_plugboard_input_int():
    pb = Plugboard()
    assert pb.translate(2) == 'C'

def test_set_plugs():
    pb = Plugboard()
    pb.setPlugs('AB EQ')
    assert pb.translate('A') == ord('B') - 65
    assert pb.translate('B') == ord('A') - 65
    assert pb.translate('E') == ord('Q') - 65
    assert pb.translate('Q') == ord('E') - 65

def test_set_then_reset_plugs():
    pb = Plugboard()
    pb.setPlugs('GH IY QB DF PU')
    pb.resetPlugs()
    assert pb.translate('G') == ord('G') - 65
    assert pb.translate('H') == ord('H') - 65
    assert pb.translate('Q') == ord('Q') - 65
    assert pb.translate('B') == ord('B') - 65