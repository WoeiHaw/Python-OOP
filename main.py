from Enemy import *
from Zombie import *
from Ogre import *

def battle(e:Enemy):
    e.talk()
    e.attack()

zombie =  Zombie(10,1)
ogre = Ogre(20,3)
print(f"{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do attack of {zombie.attack_damage}")
print(f"{ogre.get_type_of_enemy()} has {ogre.health_points} health points and can do attack of {ogre.attack_damage}")

zombie.talk()
ogre.talk()

battle(zombie)
battle(ogre)