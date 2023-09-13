
class hero:
    extra_hp = 0.05
    extra_damage = 0.05
    enough_coin = 2
    def __init__(self,name_of_hero)->None:
        self._name_of_hero = name_of_hero
        self._max_hp = 10
        self._hp = 10
        self._damage = 2
        self._level = 1
        self._coins = 0
        self._defended = False
    def __str__(self) -> str:
        return f'name of here:{self._name_of_hero} hp{self._hp} damage:{self._damage} level:{self._level} coins:{self._coins}'

    @property
    def damage(self):
        return self._damage
    @property
    def hp(self):
        return self._hp

    def change_defended(self):
        if self._defended:
            self._defended = False
        else:
            self._defended = True

    def heal(self):
        if self._hp + (self._hp *hero.extra_hp) <=self._max_hp :
            self._hp += self._hp *hero.extra_hp
        else:
            self._hp += self._max_hp

    def level_up(self):
        if self._coins >= hero.enough_coin*(self._level+1):
            self._level +=1
            self._damage += self._damage*hero.extra_damage
            self._max_hp += self._max_hp*hero.extra_damage
            self._hp = self._max_hp
        else:
            print("you dont have enough coins")

    def attack(self,monster):
        monster.reduce_health(self)
        if monster.hp == 0:
            self.increase_coins(monster.level)

    def reduce_health(self,monster):
        if self._defended:
            if self._hp - (monster.damage*0.2) >= 0:
                self._hp -= monster.damage*0.2
            else:
                self._hp = 0
        else:
            if self._hp - monster.damage >= 0:
                self._hp -= monster.damage
            else:
                self._hp = 0
        self._defended = False

    def increase_coins(self,amount_of_coins):
        self._coins += amount_of_coins
    