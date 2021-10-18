import csv
from operator import itemgetter
import copy

from rotor import Rotor
from reflector import Reflector

class ComponentBox:
    def __init__(self, rotors_path=r'parts\rotors.csv', reflectors_path=r'parts\reflectors.csv') -> None:
        self._rotor_spec_path = rotors_path
        self._reflector_spec_path = reflectors_path
        self._rotors: Rotor = []
        self._reflectors: Reflector = []
        self._alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self._generateComponents()

    def getRotor(self, name) -> Rotor:
        for rotor in self._rotors:
            if rotor.getName() == name:
                return copy.deepcopy(rotor)
        return None

    def getReflector(self, name) -> Reflector:
        for reflector in self._reflectors:
            if reflector.getName() == name:
                return reflector
        return None
    
    def listRotors(self):
        output = []
        for rotor in self._rotors:
            output.append(rotor.getName())
        return output

    def listReflectors(self):
        output = []
        for reflector in self._reflectors:
            output.append(reflector.getName())
        return output

    def _generateComponents(self):
        self._generateRotors()
        self._generateReflectors()

    def _generateRotors(self):
        with open(self._rotor_spec_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0]

                wiring = [char for char in row[1]]
                wiring_right = []
                for index in range(0, 26):
                    wiring_right.append([self._alphabet[index], wiring[index]])
                
                wiring_left = []
                for index in range(0, 26):
                    wiring_left.append([wiring[index], self._alphabet[index]])
                wiring_left = sorted(wiring_left, key=itemgetter(0))

                turnover = []
                turnover.append(row[2])
                if (row[3] != ''):
                    turnover.append(row[3])
                
                entry = Rotor(name, wiring_right, wiring_left, turnover)
                self._rotors.append(entry)

    def _generateReflectors(self):
        with open(self._reflector_spec_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name = row[0]
                wiring = [char for char in row[1]]
                final_wiring = []
                for index in range(0, 26):
                    final_wiring.append([self._alphabet[index], wiring[index]])
                entry = Reflector(name, final_wiring)
                self._reflectors.append(entry)