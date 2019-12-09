import math
import time
from math import sqrt
import random
import os
import calculator
#####EQUATIONS##########

def open_gui():
  os.system('calculator.py')

#Molarity 
def main_molarity(grams, molMass, volume):
    volume = volume/1000
    molarity = grams/molMass/volume
    return molarity

def molarity():
    grams = float(input("Enter grams of substance: "))
    molMass = float(input("Enter molar mass of substance in grams/mole: "))
    volume = float(input("Enter volume in milliliters: "))
    print("The molarity of the solution is: ", 
          format(main_molarity(grams, molMass, volume),'.2f'), " mol/L.")


#Degrees c to f or f to c conversion
def degrees():
    deg = input('Enter a for -Celcius to Fahrenheit- or b for -Fahrenheit to Celcius- : ')
    if deg == 'a':
      celsius=float(input("Enter degree: "))
      fahrenheit = (celsius * 1.8) + 32
      print('%0.1f degrees Celsius is equal to %0.1f degrees Fahrenheit' %(celsius,fahrenheit))
    elif deg == 'b':
      fahrenheit=float(input("enter degree: "))
      celcius = (fahrenheit - 32) * (5 / 9)
      print('%0.1f degrees Fahrenheit is equal to %0.1f degrees Celcius' %(fahrenheit,celcius))
    else:
      print('Please enter a valid input')
      time.sleep(3)
      degrees()


#lbs to kgs conversion
def weight():
  weight_input = input('Enter a for -Pounds to Kilograms- or b for -Kilograms to Pounds- : ')
  if weight_input == "a":
    pounds = float(input('Enter weight in Pounds(Lbs) to convert into Kilograms: '))
    kilo_grams = pounds * 0.45359237
    print(pounds,' Pounds (Lbs) are equal to', kilo_grams,'Kilograms (Kgs)')
  elif weight_input == "b":
    kilo_grams = float(input('Enter weight in Kilograms to convert into Pounds(Lbs): '))
    pounds = kilo_grams / 0.45359237
    print(kilo_grams,' Kilograms (Kgs) are equal to', pounds,'Pounds (Lbs)')
  else:
    print('Please enter a valid input')
    time.sleep(3)
    weight()


#Random Number
def randNum():
    while (True):
        i1=input("Starting Bound: ")
        i2=input("Ending Bound: ")
        try:
          i1=int(i1)
          i2=int(i2)
          if(i1>i2):
            print("Check of the order please, try again.")
            continue
          print (random.randint(i1,i2))
          break
        except:
          print('enter the correct number please, try again.')

#Trigonometric
def trig():
    while(True):
        import math
        i=input(' \nChoose a Trigonometric Operation\n1.Sine\n2.Cosine\n.Tangent\nChoice: ')
        if(i=="finish"):
          a=180
          break
        if(i!='1')&(i!='2')&(i!='3'):
          print('Look at the option clearly! Try again.')
          continue
        i2=input(" \n1.radius\n2.degree\nChoice: ")
        if(i=="finish"):
          a=180
          break
        if(i2!='1')&(i2!='2'):
          print('Look at the option clearly! Try again.')
          continue
        i3=input(' \nEnter the angle: ')
        if(i=="finish"):
          a=180
          break
        try:
          i3=eval(i3)
        except:
          print("The angle is wrong, try again.")
          continue
        if(i=="1")&(i2=="1"):
          print('The sin({}) is {}'.format(i3,math.sin(i3)))
          break
        if(i=='2')&(i2=="1"):
          print('The cos({}) is {}'.format(i3,math.cos(i3)))
          break
        if(i=='3')&(i2=='1'):
          print('The tan({}) is {}'.format(i3,math.tan(i3)))
          break
        if(i=="1")&(i2=="2"):
          i3=i3*3.14/180
          print('The sin({}) is {}'.format(i3,math.sin(i3)))
          break
        if(i=='2')&(i2=="2"):
          i3=i3*3.14/180
          print('The cos({}) is {}'.format(i3,math.cos(i3)))
          break
        if(i=='3')&(i2=='2'):
          i3=i3*3.14/180
          print('The tan({}) is {}'.format(i3,math.tan(i3)))
          break


#Sqr Root
def root():
    while (True):
        i=input("Enter the number to root: ")
        if(i=="finish"):
          a=180
          break
        i1=input('Enter the nth root: ')
        if(i1=="finish"):
          a=180
          break
        try:
          i=eval(i)
          i1=eval(i1)
          i2=i**(1/i1)
          if(i1%10==3)&(i1%100!=13):
            print('{}rd root of {} is {}'.format(i1,i,i2))
            break
          elif(i1%10==2)&(i1%100!=12):
            print('{}nd root of {} is {}'.format(i1,i,i2))
            break
          elif(i1%10==1)&(i1%100!=11):
            print('{}st root of {} is {}'.format(i1,i,i2))
            break
          elif(i1==0):
            print('The root can not be 0, try again.')
            continue
          else:
            print('{}th root of {} is {}'.format(i1,i,i2))
            break
        except:
          print('Enter numbers please, try again.')


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


#Pythagorean Theorem
def pyth():
      print('Pythagorean theorem calculator! Calculate your triangle sides.')
      print('Assume the sides are a, b, c and c is the hypotenuse (the side opposite the right angle')
      formula = input('Which side (a, b, c) do you wish to calculate? side> ')

      if formula == 'c':
        side_a = int(input('Input the length of side a: '))
        side_b = int(input('Input the length of side b: '))

        side_c = sqrt(side_a * side_a + side_b * side_b)
        
        print('The length of side c is: ' )
        print(side_c)

      elif formula == 'a':
          side_b = int(input('Input the length of side b: '))
          side_c = int(input('Input the length of side c: '))
          
          side_a = sqrt((side_c * side_c) - (side_b * side_b))
          
          print('The length of side a is' )
          print(side_a)

      elif formula == 'b':
          side_a = int(input('Input the length of side a: '))
          side_b = int(input('Input the length of side c: '))
              
          side_c = sqrt(side_c * side_c - side_a * side_a)
          
          print('The length of side b is')
          print(side_c)

      else:
        print('Please select a side between a, b, c')

############MENU###############
def print_menu():
    print(30 * "-", "Advanced Calculator Menu", 30 * "-")
    print("1. Basic Function Calculator GUI")
    print("2. Quadratic formula")
    print("3. Pythagorean Theorem")
    print("4. Molarity Function")
    print("5. Trigonometric Functions")
    print("6. Square Root Calculator")
    print("7. Random Number Generator")
    print("8. Temperature Conversion")
    print("9. Weight Conversion")
    print("10. Exit")
    print(86 * "-")

loop = True
while loop:
    print_menu()
    choice = input("Enter your choice [1-10]: ")

    if choice == '1':
        print("Menu 1 has been selected")
        open_gui()
    elif choice == '2':
        print("Menu 2 has been selected")
        quad()
        time.sleep(3)
    elif choice == '3':
        print("Menu 3 has been selected")
        pyth()
        time.sleep(3)
    elif choice == '4':
        print("Menu 4 has been selected")
        molarity()
        time.sleep(3)
    elif choice == '5':
        print("Menu 5 has been selected")
        trig()
        time.sleep(3)
    elif choice == '6':
        print("Menu 6 has been selected")
        root()
        time.sleep(3)
    elif choice == '7':
        print("Menu 7 has been selected")
        randNum()
        time.sleep(3)
    elif choice == '8':
        print("Menu 8 has been selected")
        degrees()
        time.sleep(3)
    elif choice == '9':
        print("Menu 9 has been selected")
        weight()
        time.sleep(3)

    elif choice == 'x' or 'exit' or '10':
        loop = False