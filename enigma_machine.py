from plugboard import Plugboard
from scrambler import Scrambler
from component_box import ComponentBox

class EnigmaMachine:
    def __init__(self, rotors_path=r'parts\rotors.csv', reflectors_path=r'parts\reflectors.csv') -> None:
        self._running = True

        self._scrambler = Scrambler()
        self._plugboard = Plugboard()
        self._component_box = ComponentBox(rotors_path, reflectors_path)

        self._main_menu = [
            "Select Rotors",
            "Set Rotor Positions",
            "Select Reflector",
            "Setup Plugboard",
            "Reset Plugboard",
            "Current Setup",
            "Reset to Start Positions",
            "Run Cipher",
            "Quit"
        ]

        self._rotor_select_menu = [
            ["Select the rotor for the right position (fast rotor)", "fast"],
            ["Select the rotor for the middle position (middle rotor)", "middle"] , 
            ["Select the rotor for the left position (slow rotor)", "slow"]
        ]
        
        self._rotor_position_menu = [
            ["Set the position for the right rotor (fast rotor)", "fast"],
            ["Set the position for the middle rotor (middle rotor)", "middle"],
            ["Set the position for the left rotor (slow rotor)", "slow"]
        ]

        self._reflector_select_menu = [
            "Select the reflector"
        ]

        self._plugboard_menu = [
            "Choose the letter-pairs that will be swapped with each other"
        ]

    def run(self):
        print("ENIGMA MACHINE")
        while self._running == True:
            for item in self._main_menu:
                print(str(self._main_menu.index(item) + 1)+ ">" + item)
            selection = int(input(">"))
            if (selection == 1):
                self.selectRotors()
            elif (selection == 2):
                self.setRotorPosition()
            elif (selection == 3):
                self.selectReflector()
            elif (selection == 4):
                self.insertPlugs()
            elif (selection == 5):
                self.resetPlugs()
            elif (selection == 6):
                self.printCurrentSetup()
            elif (selection == 7):
                self.resetRotorsToInitialPosition()
            elif (selection == 8):
                inputWord = input(">")
                self.runEnigmaCipher(inputWord)
            elif (selection == 9):
                self._running = False
            
    def selectRotors(self):
        for item in self._rotor_select_menu:
            print(item[0])
            for rotor in self._component_box.listRotors():
                print("Rotor # " + rotor)
            selection = input('>')
            self._scrambler.setRotor(item[1], self._component_box.getRotor(selection))

    def setRotorPosition(self):
        for item in self._rotor_position_menu:
            print(item[0])
            selection = input('>')
            self._scrambler.setRotorPosition(item[1], selection)

    def selectReflector(self):
        for item in self._reflector_select_menu:
            print(item)
            selection = input(">")
            self._scrambler.setReflector(self._component_box.getReflector(selection))

    def insertPlugs(self):
        for item in self._plugboard_menu:
            print(item)
            selection = input(">")
            self._plugboard.setPlugs(selection)

    def resetPlugs(self):
        self._plugboard.resetPlugs()
        print("Plugs removed and reset!")
    
    def resetRotorsToInitialPosition(self):
        self._scrambler.setRotorsToStartPosition()
        print("Rotors set to start position")

    def printCurrentSetup(self):
        print("Fast Rotor   - " + self._scrambler.getRotor('fast').getName() + " - " + self._scrambler.getRotor('fast').getPosition())
        print("Middle Rotor - " + self._scrambler.getRotor('middle').getName() + " - " + self._scrambler.getRotor('middle').getPosition())
        print("Slow Rotor   - " + self._scrambler.getRotor('slow').getName() + " - " + self._scrambler.getRotor('slow').getPosition())
        print("Reflector    - " + self._scrambler.getReflector().getName())
    
    def runEnigmaCipher(self, input) -> str:
        output = ''
        for letter in input:
            if (letter != ' '):
                self._scrambler.rotateRotors()
                output += self._plugboard.translate(self._scrambler.scrambleLetter(self._plugboard.translate(letter)))
        print(output)
            