# wap a program to guess the number

from random import randint
win_num = randint(1,100)

flag = False
while not flag:
    n = int(input("Enter your guess number :"))
    if win_num == n :
        print("Congrats you won")
        flag = True
    else:
        if n > win_num:
            print("Try with a smaller number,")
            continue
        else:
            print("Try with a larger number,")
            continue