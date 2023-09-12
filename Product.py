class product:
    def __init__(self, name_of_product, price, amount) -> None:
        self._name_of_product = name_of_product
        self._price = price
        self._amount = amount
        self._total_price = price * amount

    def __str__(self) -> str:
        return f"name: {self._name_of_product}, price: {self._price}, amount: {self._amount}, total price: {self._total_price}"

    @property
    def name_of_product(self):
        return self._name_of_product

    @property
    def price(self):
        return self._price

    @property
    def amount(self):
        return self._amount

    @property
    def total_price(self):
        return self._total_price

    @name_of_product.setter
    def name_of_product(self, new_name_of_product: str):
        self._name_of_product = new_name_of_product

    @price.setter
    def price(self, new_price: int):
        self._price = new_price

    @amount.setter
    def amount(self, new_amount: int):
        self._amount += new_amount

    @total_price.setter
    def total_price(self, new_total_price: str):
        self._total_price += new_total_price
