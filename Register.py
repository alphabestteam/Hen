from Costumer import costumer

class register:
    num_of_cos = 0
    def __init__(self) -> None:
        self._profit_amount = 0
        self._sales_list ={}

    # the str function is the printSummary it is the same thing so i use str
    def __str__(self) -> str:
        return f'profit amount: {self._profit_amount},sales list: {self._sales_list}'
    
    @property
    def profit_amount(self):
        return self._profit_amount
    
    @property
    def sales_list(self):
        return self._sales_list
    
    def Checkout_customer(self,new_costumer:costumer):
        register.num_of_cos +=1
        self._profit_amount += new_costumer._purchase_amount
        self._sales_list.update({register.num_of_cos: {"name ":new_costumer._name_of_costumer,"total price ":new_costumer._purchase_amount}})