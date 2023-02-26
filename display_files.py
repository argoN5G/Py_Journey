#!/usr/bin/python3
###
##

from time import sleep
from os import system
from sys import exit

def display_content():
    try:
        j = 0
        while True:
            try :
                file_name = input("Insert a file name from current directory: ") 
                file = open(file_name, "r")
                break

            except:
                j +=1
                if file_name == "q":
                    exit(0)
                else:
                    print("Please insert a valid file name or (Exit press: q )")


        done = False
        i = 0
        while not done:
            char = file.read(1)
            print(char, end="", flush=True)
            sleep(0.01)
            if char == "":
                i +=1
                if i == 2:
                    done = True
                    sleep(1)
                    system('clear')
                    system("echo Done! what are you waiting for !!!!")
                    exit(0)

    except:
        pass
        #exit(0)

display_content()
