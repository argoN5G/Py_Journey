#!/usr/bin/python3
##
###
from sys import exit

def say_Hi():
    try:
        name = input("ISERT YOUR NAME : ")
        print("\tHi!  %s\n\tHave a good day!"%str(name))
    
    except:
        exit(0)


say_Hi()
