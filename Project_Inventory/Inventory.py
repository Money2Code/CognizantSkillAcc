class inventory():
    def __init__(self,inventory):
        self.inventory = inventory
        print(inventory)

    def intial_inventory(self, inventory):
        print(inventory)
    

    def add_fruit(self):
        fruit_name= input("enter the Fruit to add to the inventory")
        quantity = int(input("enter the quantity of "+fruit_name))
        price= int(input("enter the price of "+fruit_name ))
        if isinstance(self.inventory, dict):
            self.inventory[fruit_name] = {"quantity":quantity,"price" :price}
        else:
            print("inventory is not a dictionary")
        return self.inventory

    def remove_fruit(self):
        fruit_name= input("enter the fruit to remove")
        if fruit_name in self.inventory:
            del self.inventory[fruit_name]
        else:
            print("fruit not found")
        
        return self.inventory
    
    def update_quantity(self):
        fruit_name= input("enter the fruit to update quantity")
        if fruit_name in self.inventory:
            new_quantity = int(input("enter new quantity of "+fruit_name))
            self.inventory[fruit_name]["quantity"] = new_quantity
        else:
            print("fruit not found")
        
        return self.inventory
    
    def calculate_total(self):
        total_price=0
        for key,value in self.inventory.items():
            total_price+=value["quantity"]*value["price"]  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of all fruits  # calculate total price of
            
        return total_price
    
inventory_data= {}

apple_quantity = int(input("enter quantity of apple"))
apple_price=int(input("enter price per apple" ))

banana_quantity = int(input("enter quantity of banana"))
banana_price=int(input("enter price per banana" ))


inventory_data["apple"] = {"quantity": apple_quantity, "price": apple_price}
inventory_data["banana"] = {"quantity": banana_quantity, "price": banana_price}


obj1=inventory(inventory_data)
val1=obj1.intial_inventory(inventory_data)
print(val1)

val2=obj1.add_fruit()
print(val2)

val56=obj1.remove_fruit()
print(val56)

val4=obj1.update_quantity()
print(val4)

val5=obj1.calculate_total()
print(val5)