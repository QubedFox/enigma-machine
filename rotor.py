class Rotor:
    def __init__(self, name, wiring_right, wiring_left, turnover) -> None:
        self._name: str = name
        self._wiring_right: list = wiring_right
        self._wiring_left: list = wiring_left
        self._turnover: list = turnover

    def getName(self):
        return self._name
    
    def getPosition(self):
        return self._wiring_right[0][0]

    #FRom the plugboard to the reflector
    def rightToLeft(self, position):
        output = self._wiring_right[position][1]
        for index in range(0, 26):
            if (self._wiring_right[index][0] == output):
                return index

    #From the reflector to the plugboard
    def leftToRight(self, position):
        output = self._wiring_left[position][1]
        for index in range(0, 26):
            if (self._wiring_left[index][0] == output):
                return index

    def rotate(self):
        new_wiring_right = []
        new_wiring_left = []

        for index in range(-25, 1):
            new_wiring_right.append(self._wiring_right[index])
        for index in range(-25, 1):
            new_wiring_left.append(self._wiring_left[index])

        self._wiring_right = new_wiring_right
        self._wiring_left = new_wiring_left
        
    def setPosition(self, letter):
        self.rotate()
        while self.getPosition() != letter:
            self.rotate()

    def hasTurnedover(self):
        for index in range(0, len(self._turnover)):
            if (self._wiring_right[0][0] == (self._turnover[index])[1]):
                return True
        return False
    
    def inTurnoverPosition(self):
        for index in range(0, len(self._turnover)):
            if (self._wiring_right[0][0] == (self._turnover[index])[0]):
                return True
        return False