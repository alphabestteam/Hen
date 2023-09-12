import json
from Product import product
from Costumer import costumer
from Register import register


def add_data(data: dict, num: int, costumer: costumer):
    name = costumer.name_of_costumer
    cart = [p for p in costumer._shopping_list]
    total = costumer._purchase_amount
    data[num] = {"name:": name, "cart:": cart, "total:": total}


def main():
    # I make 5 registers dont ask me why 5 hahaha
    registers = [register() for _ in range(0, 5)]
    data = {}
    num = 1
    print(
        "for add product enter 1 for remove 2 and for end shop 3 for go to register and make new costumer 4"
    )
    next_move = int(input("enter what you want to do next"))
    name = input("for start shopping enter your name")
    cos = costumer(name)
    while next_move != 3:
        if next_move == 1:
            name_of_product = input("enter the name of the product")
            price = int(input("enter the price of the product"))
            amount = int(input("enter the amount of the product"))
            p = product(name_of_product, price, amount)
            cos.add_product(p)
        elif next_move == 2:
            name_of_product = input("enter the name of the product")
            price = int(input("enter the price of the product"))
            amount = int(input("enter the amount of the product"))
            p = product(name_of_product, price, amount)
            cos.remove_product(p)
        elif next_move == 4:
            choose_register = int(
                input(
                    "enter the number of register you want to pay in between 0-5 not include 5"
                )
            )
            registers[choose_register].Checkout_customer(cos)
            add_data(data, num, cos)
            num += 1
            name = input("for start shopping new costumer enter your name")
            cos = costumer(name)
        else:
            pass
        print(data)
        next_move = int(input("enter what you want to do next"))

    for _ in range(len(registers)):
        print(registers[_])

    new_f = open("items.json", "a")
    new_f.write(json.dumps(data))
    new_f.close()


if __name__ == "__main__":
    main()
