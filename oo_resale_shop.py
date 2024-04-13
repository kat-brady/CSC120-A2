from typing import Dict
from computer import *
"""
ResaleShop class runs the OOP computer resale shop, intended to
simulate sale of computers
"""
class ResaleShop:
    """
    The constructor for resale shop, which creates an empty list for
    the shop's inventory and sets the initial item_id equal to 0
    """
    def __init__(self):
        self.inventory : Dict[int, Dict] = {}
        #self.inventory= {}
        self.item_id=0
    """
    The buy function takes self and computer, an object of the Computer
    class, as arguments. It adjusts the item_id and adds computer to
    the shop's inventory, returning the item_id
    """
    def buy(self, computer:Computer):
        self.item_id += 1
        self.inventory[self.item_id]=computer
        return self.item_id
    """
    The sell function takes self and int item_id as arguments, allowing
    the shop to remove a computer from the inventory if its item_id
    was previously stored there
    """
    def sell(self, item_id:int):
        if item_id in self.inventory:
           print("Selling item", item_id)
           del self.inventory[item_id]
        else:
           print("The item", item_id,"could not be found in the inventory.")
    """
    The print_inventory function takes self as an argument and displays
    the description of each computer found to have its item_id in
    the shop's inventory
    """
    def print_inventory(self):
        if self.inventory:
            for item_id in self.inventory:
                print(f'Item ID: {item_id} : {self.inventory[item_id].description}, {self.inventory[item_id].processor_type}, {self.inventory[item_id].hard_drive_capacity} GB capacity, {self.inventory[item_id].memory} MB memory, {self.inventory[item_id].operating_system}, made in {self.inventory[item_id].year_made}, ${self.inventory[item_id].price}')
        else:
            print("No inventory to display.")
    """
    The update_price function takes self, int item_id, and int new_price
    as arguments. It allows the price of the computer to be updated if
    its item_id is in the inventory
    """
    def update_price(self, item_id:int, new_price:int): 
        if item_id in self.inventory:
            self.inventory[item_id].price = new_price
            print("The price has been updated to $",new_price)
        else:
            print("The item could not be found in the inventory, so the price cannot be updated.")
    """
    The refurbish function takes self, int item_id, and string new_os
    as arguments. It updates the price of the computer according to
    the year it was made, and adjusts the operating system accordingly.
    If the item_id is not already in the inventory, it will not perform
    the above actions.
    """
    def refurbish(self, item_id:int, new_os:str=None):
        if item_id in self.inventory:
            if self.inventory[item_id].year_made<2000:
               self.inventory[item_id].price = 0
            elif self.inventory[item_id].year_made < 2012:
                self.inventory[item_id].price = 250
            elif self.inventory[item_id].year_made < 2018:
                self.inventory[item_id].price = 550
            else:
                self.inventory[item_id].price = 1000
            if new_os is not None:
                self.inventory[item_id].operating_system = new_os
            print("Refurbishing computer...\nSuccess! The price is now $", self.inventory[item_id].price , "and the operating system is" , self.inventory[item_id].operating_system,".")
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

def main():
    computer: Computer=Computer("2019 MacBook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)
    shop: ResaleShop=ResaleShop()
    shop.buy(computer)
    shop.print_inventory()
    shop.update_price(1, 30)
    shop.refurbish(1)
    print(computer.price)


main()