from Enemy import *
    
zombie = Enemy()

# print(zombie.talk()) 
# will throw err AttributeError: 'Enemy' object has no attribute 'type_of_enemy'

# first assign value to atribute type_of_enemy

zombie.type_of_enemy="Zombie"
print(zombie.talk()) # I am a Zombie. Be prepared!
print(zombie.walk_forward()) # Zombie attacking you. Your health point is 10
