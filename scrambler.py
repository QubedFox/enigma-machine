from rotor import Rotor
from reflector import Reflector

class Scrambler:
    def __init__(self) -> None:
        self._fast_rotor: Rotor
        self._middle_rotor: Rotor
        self._slow_rotor: Rotor
        self._reflector: Reflector
        self._starting_positions = [['fast', ''],['middle', ''],['slow','']]
    
    def setReflector(self, reflector: Reflector):
        self._reflector = reflector

    def getReflector(self) -> Reflector:
        return self._reflector        
    
    def setRotor(self, position, rotor: Rotor):
        if position == 'fast':
            self._fast_rotor = rotor
        elif position == 'middle':
            self._middle_rotor = rotor
        elif position == 'slow':
            self._slow_rotor = rotor

    def getRotor(self, position) -> Rotor:
        if position == 'fast':
            return self._fast_rotor
        elif position == 'middle':
            return self._middle_rotor
        elif position == 'slow':
            return self._slow_rotor
    
    def setRotorPosition(self, position, letter):
        if position == 'fast':
            self._starting_positions[0][1] = letter
            self._fast_rotor.setPosition(letter)
        elif position == 'middle':
            self._starting_positions[1][1] = letter
            self._middle_rotor.setPosition(letter)
        elif position == 'slow':
            self._starting_positions[2][1] = letter
            self._slow_rotor.setPosition(letter)
    
    def setRotorsToStartPosition(self):
        for position in self._starting_positions:
            self.setRotorPosition(position[0], position[1])
    
    def scrambleLetter(self, position):
        position = self._fast_rotor.rightToLeft(position)
        position = self._middle_rotor.rightToLeft(position)
        position = self._slow_rotor.rightToLeft(position)

        position = self._reflector.reflect(position)

        position = self._slow_rotor.leftToRight(position)
        position = self._middle_rotor.leftToRight(position)
        position = self._fast_rotor.leftToRight(position)

        return position
    
    def rotateRotors(self):
        self._fast_rotor.rotate()
        if (self._fast_rotor.hasTurnedover() == True):
            self._middle_rotor.rotate()
            if (self._middle_rotor.hasTurnedover() == True):
                self._slow_rotor.rotate()
        elif (self._fast_rotor.hasTurnedover() == False):
            if (self._middle_rotor.inTurnoverPosition() == True):
                self._middle_rotor.rotate()
                self._slow_rotor.rotate()
    
    def getRotorPositions(self) -> str:
        return self._slow_rotor.getPosition() + '-' + self._middle_rotor.getPosition() + '-' + self._fast_rotor.getPosition()