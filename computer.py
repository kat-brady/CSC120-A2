""" 
The Computer class handles the details about the computers themselves,
including establishing their features and creating a constructor for a computer
"""
class Computer: 
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    """ 
    This is the constructor for computer, which takes self,
    String description, String processor_type, int hard_drive_capacity,
    int memory, String operating_system, int year_made,
    and int price as arguments to construct a computer with all those attributes
    """
    def __init__(self, description:str, processor_type:str, hard_drive_capacity:int, memory:int, operating_system:str, year_made:int, price:int):
        self.description=description
        self.processor_type=processor_type
        self.hard_drive_capacity=hard_drive_capacity
        self.memory=memory
        self.operating_system=operating_system
        self.year_made=year_made
        self.price=price