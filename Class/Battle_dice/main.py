from game import Game
from character import Character
from charactertype import CharacterType

#Create characters
alice = Character(name="Alice" , character_type=CharacterType.WARRIOR, health=100, attack)
bob = Character(name="Bob" , character_type=CharacterType.MAGE, health=70, attack_powers=)

#Start game
game = Game (alice, bob)
game . start_battle()
