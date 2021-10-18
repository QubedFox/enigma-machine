#The plugsboard functionality it to change the electrical path (or in
# our case the logical path) that comes from the input of the keyboard 
#and output of the fast rotor.
class Plugboard:
    def __init__(self) -> None:
        self._ASCII_OFFSET = 65
        self._board = [
            ['A','A'],['B','B'],['C','C'],['D','D'],['E','E'],['F','F'],
            ['G','G'],['H','H'],['I','I'],['J','J'],['K','K'],['L','L'],
            ['M','M'],['N','N'],['O','O'],['P','P'],['Q','Q'],['R','R'],
            ['S','S'],['T','T'],['U','U'],['V','V'],['W','W'],['X','X'],
            ['Y','Y'],['Z','Z']]
    
    def setPlugs(self, input):
        connections = []
        input_array = input.split()
        for link in input_array:
            temp = [char for char in link]
            connections.append(temp)

        for index in range(len(connections)):
            insert_position = self._charToAscii(connections[index][0])
            self._board[insert_position][1] = connections[index][1]

            insert_position = self._charToAscii(connections[index][1])
            self._board[insert_position][1] = connections[index][0]
    
    def getPlugs(self):
        return self._board

    def resetPlugs(self):
        for index in range(26):
            self._board[index][1] = self._board[index][0]

    def translate(self, input):
        if type(input) is str:
            entry_position = self._charToAscii(input)
            return self._charToAscii(self._board[entry_position][1])
        elif type(input) is int:
            return self._board[input][1]

    #Converts a letter input into its position on exit
    #of the plugboard. Later functionality will include
    #inserting "plugs" into the board
    def _charToAscii(self, letter):
        return ord(letter) - self._ASCII_OFFSET
    
    ##Converts an output of the scrambler (a position) into
    ##a readable letter for the user
    #def asciiToChar(self, position):
    #    return chr(position + self._ASCII_OFFSET)