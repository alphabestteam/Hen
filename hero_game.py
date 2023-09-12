from Hero import hero
from Monster import monster

def choose_action(h:hero,m:monster):
    print("for heal print h , for up level print u, for defend print d ,for attack print a")
    action = input("enter you action:")
    if action == "a":
        h.attack(m)
    elif action == "h":
        h.heal()
    elif action == "d":
        h.change_defended()
    elif action == "u":
        h.level_up()

def main():
    h = hero("hen")
    m = monster("bla",h._level)
    print(h)
    print(m)
    while h.hp != 0:
        print("turn of hero")
        choose_action(h,m)
        if m.hp == 0:
            print("very good you kill a monster here is another one")
            m = monster("bla",h._level)
        print("now the monster attack")
        m.attack(h)
        print(h)
        print(m)
        h.increase_coins(1)
    print("you fought well but the monsters wins lets try again")
        


if __name__ == "__main__":
    main()