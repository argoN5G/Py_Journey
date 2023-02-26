#!/usr/bin/python3
##
###
# this code print out it self

import sys
from os import system
import time

def load():
    t = time.time()
    p = 10
    s = 0.2
    t += p
    i = 1
    while t > time.time():
        var = "Loading please Wait:\n[ " + "#"*i + " " + str(i*100/(p/s))+"% ]"
        print(var)
        time.sleep(s)
        system('clear')
        i += 1
    print("# Done!    100%")


def read_file(file_name):
    file = open(file_name, 'r')
    load()
    done = False
    while not done: # True
        char = file.read(1)
        print(char, end='', flush=True)
        time.sleep(0.03)
        if char == "":
            done = True


try:
    system("clear")
    read_file("display_self.py")

except:
    sys.exit(0)
