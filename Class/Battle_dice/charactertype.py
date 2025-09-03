from enum import Enum
class CharacterType(Enum):
    WARRIOR = "Warrior"
    MAGE = "Mage"
    ROGUE = "Rogue"

# Instantiating an Enum member
mycharactertype = CharacterType.WARRIOR
# Accessing name and value
print(mycharactertype) # Output : CharacterType.WARRIOR
print (mycharactertype.name ) # Output : ”WARRIOR”
print (mycharactertype.value) # Output : ”Warrior”
