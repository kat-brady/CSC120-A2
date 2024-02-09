from computer import *
#This creates the class used for the shop
class ResaleShop:
    #inventory= {}
   # item_id=0
    
    def __init__(self): #This is the constructor
        #self.inventory=inventory
        #self.item_id=item_id
        self.inventory= {}
        self.item_id=0
    def buy(self, computer:Computer): #This function allows the shop to buy computers
       # id=self.item_id+1
        #computer=Computer[id]
        self.item_id += 1
        self.inventory[self.item_id]=computer
        return self.item_id
    def sell(self, item_id:int): #This function sells computers
        if item_id in self.inventory:
           print("Selling item", item_id)
           del self.inventory[item_id]
        else:
           print("The item", item_id,"could not be found in the inventory.")
    def print_inventory(self): #This function shows what is in the inventory
        if self.inventory:
            for item_id in self.inventory:
                print(f'Item ID: {item_id} : {self.inventory[item_id].description}')
        else:
            print("No inventory to display.")
    def update_price(self, item_id:int, new_price:int): #This function updates the prices of computers
        if item_id in self.inventory:
            self.inventory[item_id] = new_price
            print("The price has been updated to $",new_price)
        else:
            print("The item could not be found in the inventory, so the price cannot be updated.")
    def refurbish(self, item_id:int, new_os:str=None): #This function refurbishes the purchased computers
        if item_id in self.inventory:
            computer=self.inventory[item_id]
            if computer.year_made<2000:
               computer.price = 0
            elif computer.year_made < 2012:
                computer.price = 250
            elif computer.year_made < 2018:
                computer.price = 550
            else:
                computer.price = 1000
            if new_os is not None:
                computer.operating_system = new_os
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

#def main():
    #computer: Computer=Computer("2019 MacBook Pro", "Intel",256, 16, "High Sierra", 2019,1000)
    #shop: ResaleShop=ResaleShop()
    #print(shop.buy(computer))
    #shop.print_inventory()
    #shop.update_price(1, 30)
    #shop.refurbish(1)
    #print(computer.price)


#main()