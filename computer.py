class Computer: #This class is created to deal with each individual computer
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
   #This is the constructor
    def __init__(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:int):
        self.description=description
        self.processor_type=processor_type
        self.hard_drive_capacity=hard_drive_capacity
        self.memory=memory
        self.operating_system=operating_system
        self.year_made=year_made
        self.price=price
    def refurbish(self, item_id:int, new_os:str=None): #This function refurbishes the purchased computers
       if item_id in self.inventory:
            computer=self.inventory[item_id]
            if int(computer["year_made"])<2000:
               computer["price"] = 0
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550
            else:
                computer["price"] = 1000
            if new_os is not None:
                computer["operating_system"] = new_os
            else:
                print("Item", item_id, "not found. Please select another item to refurbish.")