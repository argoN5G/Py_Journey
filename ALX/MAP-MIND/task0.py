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
    #Lst = []   # uncomment this line if take_inputs
    input_numbers = [1,2,4,6,8,10]
    Sum = 0
    # uncomment the line below if wanting to take user inputs
    #take_input(Lst)
    
    for i in input_numbers: # Lst if take_inputs
        Sum += i**2

    return Sum

result = squares_sum()
print(result)
