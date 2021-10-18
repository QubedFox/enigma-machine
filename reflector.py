#The reflector in the enigma machine allowed for there to be one
#setting rather than a seperate encode and decode setting
class Reflector:
    def __init__(self, name, wiring) -> None:
        self._name = name
        self._wiring = wiring

    def getName(self):
        return self._name

    def reflect(self, position):
        output = self._wiring[position][1]
        for index in range(0, 26):
            if (self._wiring[index][0] == output):
                return index
    