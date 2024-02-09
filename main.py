# Import a few useful containers from the typing module
#from typing import Dict, Union

from oo_resale_shop import *
from computer import *

def main():
    #Make a computer to add and make sure the shop is good to go
    computer=Computer("2019 MacBook Pro", "Intel",256, 16, "High Sierra", 2019,1000)
    shop=ResaleShop()

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    shop.buy(computer)

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    shop.refurbish(1, new_OS)
    print("The computer now costs $", computer.price)
    print("The new operating system is", new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    shop.sell(1)
    print("The item was successfully sold.\n")
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    shop.print_inventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()
