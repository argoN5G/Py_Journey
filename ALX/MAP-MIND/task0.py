#!/usr/bin/python3

def take_input(List):
    i = 0
    while True:
        try:
            if i < 1:
                print("Press q to break after entering numbers!!'")
                i += 1
            user_input = input("Enter a Number: ")
            List.append(int(user_input))

        except:
            if user_input == 'q':
                break
            else:
                print("Press 'q' to break or Insert integer number!")
                

def squares_sum():
    Lst = []
    Sum = 0
    take_input(Lst)
    
    for i in Lst:
        Sum += i**2

    return Lst, Sum

numbers, result = squares_sum()
print("Sum of %s squares: %s"%(numbers, result))
