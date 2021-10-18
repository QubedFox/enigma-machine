from enigma_machine import EnigmaMachine

em = EnigmaMachine(rotors_path=r'parts\rotors.csv', reflectors_path=r'parts\reflectors.csv')
em.run()
