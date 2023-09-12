import random
def random_values():
    final_name = random.choice(["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Isaac", "Julia"])
    final_age = random.choice([55,34,67,43,26,75,12,56,23,54])
    final_id = random.choice([234543,483294,684833,678483,594939,583933,384383,392929,358393,567328])
    return final_name , final_age,final_id

class person:
    
    def __init__(self):
        name , age , id = random_values()
        self.name = name
        self.id = id
        self.age = age

    def print_name(self):
        return self.name
    def print_id(self):
        return self.id
    def print_age(self):
        return self.age

    def change_name(self,new_name):
        self.name = new_name
    def change_id(self,new_id):
        self.id = new_id
    def change_age(self,new_age):
        self.age = new_age

    def __str__(self):
        return f"the name is {self.name} the age is {self.age} and the id is {self.id}"