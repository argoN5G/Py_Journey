#!/usr/bin/python3
##

def moveFrom(f,t):
    print("Move disc from {} to {}!".format(f,t))

def moveVia(f,v,t):
    moveFrom(f,v)
    moveFrom(v,t)


# n = number of disks
# f = from position
# h = helper position
# t = target position
i = 0
def hanoi(n,f,h,t):
    global i
    if n == 0:
        pass
    else:
        hanoi(n-1,f,t,h)
        moveFrom(f,t)
        hanoi(n-1,h,f,t)
        i +=1

hanoi(4,"A","B","C")
print(i, " moves.")

