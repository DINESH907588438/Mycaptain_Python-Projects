import math
S=' CALCULATOR '
m="🌹"
print(S.center(30,m))
print("Options\n\n 1.Add\n 2.Subraction \n 3.Multiplication\n 4.Divison\n 5.Power")
print(" 6.Reminder \n 7.sin value \n 8.cos value \n 9.square root \n 10.ASCII value\n 11.Character for the Given ASCII value\n 12.Square of a number\n")
opt = int(input("Enter Your Option NO: "))
print('\n')
if opt <=6:
    x1 = int(input('Enter the Value for number 1: '))
    x2 = int(input('Enter the Value for number 2: '))

    if opt == 1:
        print("{} + {} = {}".format(x1,x2,x1+x2))
    elif opt == 2:
        print("{} - {} = {}".format(x1,x2,x1-x2))
    elif opt == 3:
        print("{} * {} = {}".format(x1,x2,x1*x2))
    elif opt == 4:
        print("{} / {} = {}".format(x1,x2,x1/x2))
    elif opt == 5:
        print("{} ** {} = {}".format(x1,x2,x1**x2))
    elif opt == 6:
        print("{} % {} = {}".format(x1,x2,x1%x2))
if opt <=12:
    if opt == 7:
        S=float(input('Enter the number to find sin value: '))
        print("sin({}) = ".format(S),end='')
        print(math.sin(S))

    elif opt == 8:
        S=float(input('Enter the number to find cos value: '))
        print("cos({}) = ".format(S),end='')
        print(math.cos(S))
    elif opt == 9:
        S=int(input("Enter the number to find square root: "))
        print("sqaureroot ({})= ".format(S),end='')
        print(math.sqrt(S))

    elif opt == 10:
        S=input("Enter your character: ")
        print("ASCII({}) = {}".format(S,ord(S)))
    elif opt == 11:
        S=int(input("Enter the ASCII value: "))
        print("Character({}) = {}".format(S,chr(S)))

    elif opt == 12:
        S=int(input('Enter the number to find sqaure: '))
        print("Sqaure({}) = {}".format(S,S**2))
else:
    print('(: Please,Enter the Valid option :)')























