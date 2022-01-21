#!/usr/bin/env python3

import classes
import random

def moving(drive_transport):
    print("-"*30, "\n")

    for item in drive_transport:
        item.move(int(random.random()*250))
    print("-"*30, "\n")    

    classes.print_transport(drive_transport)
 

def main():
    """Demonstrate a create different classes of transport and changing speed"""
    print(main.__doc__, "\n", "-"*30)
    drive_transport = [classes.Automotive("Mercedes", "s500", "240", "2600",
                                         "4"),
                      classes.Automotive("Audi", "T8", "220", "1900", "4"),
                      classes.Aircraft("Boeing", "703", 1200, 5300,
                                       "Airplane"),
                      classes.Boat("K19", "D5", 55, 450, 1),
                      classes.Train("TP12", "WE1", 110, 63000, "diesel")]

    print("List of all transport:")
    print("-"*30, "\n")
    classes.print_transport(drive_transport)    
    print("\nSome transport now move:")
    moving(drive_transport)
    print("\nSome transport now move:")
    moving(drive_transport)


main()
