import random
from Hero import hero

class monster:
    damage_hp = 1.5
    def __init__(self,name_of_monster,level_of_hero)->None:
        self._name_of_monster = name_of_monster
        self._level = random.randint(level_of_hero-1,level_of_hero+1)
        self._hp = self._level * monster.damage_hp + 1
        self._damage = self._level* monster.damage_hp +1
    def __str__(self) -> str:
        return f'name:{self._name_of_monster} level:{self._level} hp:{self._hp} damage:{self._damage}'

    @property
    def hp(self):
        return self._hp
    @property
    def level(self):
        return self._level
    @property
    def damage(self):
        return self._damage

    def attack(self,my_hero:hero):
        my_hero.reduce_health(self)

    def reduce_health(self,my_hero:hero):
        if self._hp - my_hero.damage >= 0:
            self._hp -= my_hero._damage
        else:
            self._hp = 0
        