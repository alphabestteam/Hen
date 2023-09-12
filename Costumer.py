from Product import product

def product_exist(name_of_product,shopping_list:dict):
    if name_of_product in shopping_list:
        return True
    return False
def p_shopping_list(shopping_list:dict):
    for product in shopping_list:
        print(product)

class costumer:
    def __init__(self,name_of_costumer)->None:
        self._name_of_costumer = name_of_costumer
        self._shopping_list = {}
        self._purchase_amount = 0

    def __str__(self) -> str:
        return f'name : {self._name_of_costumer}, shopping list : {self._shopping_list}, purchase amount : {self._purchase_amount}'
    
    @property
    def name_of_costumer(self):
        return self._name_of_costumer
    
    @property
    def shopping_list(self):
        return self._shopping_list
    
    @property
    def purchase_amount(self):
        return self.purchase_amount

    
    @name_of_costumer.setter
    def name_of_costumer(self,new_name_of_costumer:str):
        self._name_of_costumer = new_name_of_costumer
    
    def add_product(self,new_product:product):
        if product_exist(new_product.name_of_product,self.shopping_list):
            self._shopping_list[new_product.name_of_product].amount = new_product.amount
            self._shopping_list[new_product.name_of_product].total_price = new_product.amount* self._shopping_list[new_product.name_of_product].price
            self._purchase_amount += new_product.amount* self._shopping_list[new_product.name_of_product].price
        else:
            self._shopping_list[new_product.name_of_product]= new_product
            self._purchase_amount += new_product.total_price

    def remove_product(self,new_product:product):
        if product_exist(new_product.name_of_product,self.shopping_list):
            if new_product.amount >= self._shopping_list[new_product.name_of_product].amount:
                self._purchase_amount -= self._shopping_list[new_product.name_of_product].amount* self._shopping_list[new_product.name_of_product].price
                self._shopping_list.pop(new_product.name_of_product)
            else:
                self._shopping_list[new_product.name_of_product].amount = -new_product.amount
                self._shopping_list[new_product.name_of_product].total_price = -(new_product.amount* self._shopping_list[new_product.name_of_product].price)
                self._purchase_amount -= new_product.amount* self._shopping_list[new_product.name_of_product].price
        else:
            print("the product you want to remove dont exist")
    
    @purchase_amount.setter
    def purchase_amount(self,new_purchase_amount:int):
        self._purchase_amount = new_purchase_amount