def product_exists(name,list_of_dicts):
    return any(name in _ for _ in list_of_dicts)

def position_of_product(name,list_of_dicts):
    for index in range(len(list_of_dicts)):
        if name in list_of_dicts[index]:
            return index

print("enter your next step ")
print("1 for add product ")
print("2 for remove product ")
print("3 for end shopping ")

shopping_cart = []
total_price = 0

shopping_status = int(input("enter what you want to do "))
while shopping_status != 3:
    if shopping_status ==1:
        name_of_product = input("enter the name of the product ")
        price_of_product = int(input("enter the price of the product "))
        amount_of_product = int(input("enter the amount of the product "))
        if product_exists(name_of_product,shopping_cart):
            position = position_of_product(name_of_product,shopping_cart)
            print(position)
            new_amount = shopping_cart[position][name_of_product]["amount"] + amount_of_product
            shopping_cart[position][name_of_product]["amount"] = new_amount
            total_price += price_of_product*amount_of_product
        else:
            shopping_cart.append({name_of_product:{"price":price_of_product,"amount":amount_of_product}})
            total_price += price_of_product*amount_of_product
    elif shopping_status ==2:
        name_of_product = input("enter the name of the product ")
        amount_of_product = int(input("enter the amount of the product "))
        if product_exists(name_of_product,shopping_cart):
            position = position_of_product(name_of_product,shopping_cart)
            if amount_of_product > shopping_cart[position][name_of_product]["amount"]:
                print("you dont have this amount in your cart try again ")
            elif amount_of_product < shopping_cart[position][name_of_product]["amount"]:
                new_amount = shopping_cart[position][name_of_product]["amount"] - amount_of_product
                price = shopping_cart[position][name_of_product]["price"]
                shopping_cart[position][name_of_product]["amount"] = new_amount
                total_price -= (price * amount_of_product)
            else:
                price = shopping_cart[position][name_of_product]["price"]
                total_price -= amount_of_product*price
                del shopping_cart[position]
    print(shopping_cart)
    shopping_status = int(input("enter what you want to do "))

print(f"the total shopping cant {shopping_cart}")
print(f"the total price is {total_price}")