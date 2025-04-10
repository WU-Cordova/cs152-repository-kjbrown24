import random
from charactertype import CharacterType

class Game:
    """Manages the Dice Battle game logic ."""
    
    def __init__(self, player1: Character, player2: Character):
        """Initializes the game with two players."""
        self. __player1 = player1
        self. __player2 = player2

    def attack (self, attacker: Character, defender: Character):
        """ Performs an attack where the attacker rolls a die to determine damage dealt."""
        pass  #TODO: Implement die roll )1-6) and apply scaled attack power to defender
    def start_battle(self):
        """Starts a turn based battle between two players."""
        pass #TODO: implement the battle loop wehre players take turns attacking





















# Instantiating an Enum member
mycharactertype = CharacterType.WARRIOR
# Accessing name and value
print(mycharactertype) # Output : CharacterType.WARRIOR
print (mycharactertype.name ) # Output : ”WARRIOR”
print (mycharactertype.value) # Output : ”Warrior”
