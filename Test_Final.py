import math
import time
#####EQUATIONS##########

#Quadratic Formula
def quad():

    a = int(input("Enter the coefficients of a: "))
    b = int(input("Enter the coefficients of b: "))
    c = int(input("Enter the coefficients of c: "))

    d = b**2-4*a*c # discriminant

    if d < 0:
        print ("This equation has no real solution")
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        print ("This equation has one solutions: "), x
    else:
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        print ("This equation has two solutions: ", x1, " or", x2)

    time.sleep(5)


############MENU###############
def print_menu():  ## Your menu design here
    print(30 * "-", "MENU", 30 * "-")
    print("1. Menu Option 1")
    print("2. Menu Option 2")
    print("3. Menu Option 3")
    print("4. Menu Option 4")
    print("5. Exit")
    print(67 * "-")

loop = True
while loop:
    print_menu()
    choice = input("Enter your choice [1-5]: ")

    if choice == '1':
        print("Menu 1 has been selected")
        quad()
    elif choice == '2':
        print("Menu 2 has been selected")
        threes()

    elif choice == '5':
        loop = False