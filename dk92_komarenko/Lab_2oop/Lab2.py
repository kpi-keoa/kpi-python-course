#!/usr/bin/env python3

import classes


def main():
    print('Start Lab2 with use module classes.py\n'
          '--------------------------------')
    sale_transport = [classes.Automotive("Mercedes", "s500", "240", "2600",
                                         "4"),
                      classes.Aircraft("Boeing", "703", 1200, 5300,
                                       "Airplane"),
                      classes.Boat("K19", "D5", 55, 450, 1),
                      classes.Train("TP12", "WE1", 110, 63000, "diesel")]
    for item in sale_transport:
        print(item)
        print()


main()
