#!/usr/bin/python3

from time import sleep
from sys import exit

def fibonatchi():
    i = 0
    j = 1
    List = []
    while j < 101:
        try:
            z = i + j
            print("%s + %s = %s"%(i,j,z))
            List.append(z)
            i = z
            j += 1
            sleep(0.2)

        except:
            exit(0)
    print(List)


fibonatchi()
