
a=1
while(a==1):
  def menu():
    global x
    def addition():
      while(True):
        sum=0
        i=input('Enter the numbers separated by a space to be added: ')
        if(i=="finish"):
          a=18
          break
        try:
          l2=i.split()
          for s in range(len(l2)):
            sum+=int(l2[s])
          print('The sum of those numbers are: ',sum)
          print()
          break
        except:
          print("Please enter numbers, try again.")
          print()

    #molarity not working properly    
    import math
    def molarity(d_nm=17, peak_od=0.93, path_length_cm=1,
      density_g_per_cm3=19.28,
      molar_Extinction_perM_percm=3.68E8):

      print('\nInput parameters :\n')

      print('Diameter of particle: {} nm'.format(d_nm))
      print('Density of metal: {} g/cm^2'.format(density_g_per_cm3))
      print('Measured peak_OD: {}'.format(peak_od))
      print('Cuvvette path length: {} cm'.format(path_length_cm))
      print('Assumed Molar Extinction : {:.2E} (M-1Cm-1)'.format(molar_Extinction_perM_percm))

      print('\nOutput parameters :\n')

      C_M = peak_od / (path_length_cm * molar_Extinction_perM_percm) # Beer-Lambert Law
      print('Concentration of Nanoparticles (M, moles of particles/1L of solvent) : {:.3E}'.format(C_M))

      # convert molarity to NPS/ml ( Nanoparticles per ml), here Molarity refers to N Nps per 1000 ml
      NPS_per_ml = C_M * 6.0221409e+23 / 1000
      print('Nanoparticles per ml : {:.3E}'.format(NPS_per_ml))

      # Calculate weight of each Particle
      np_weight_g = math.pi * ((d_nm / 2.0) * 1E-7) ** 3 * density_g_per_cm3
      print('Weight of each particle (g) : {:.3E}'.format(np_weight_g))

      # Convert Molarity (moles of particles/1L of solvent) to weight_concentration_ug_ml
      weight_concentration_ug_per_ml = NPS_per_ml * (4.0 / 3) * np_weight_g * 1E6
      print('Weight_concentration (ug/ml) : {:.3f}'.format(weight_concentration_ug_per_ml))
      print(molarity(d_nm=17, peak_od=0.93, path_length_cm=1,
      density_g_per_cm3=19.28,
      molar_Extinction_perM_percm=3.68E8))

    # quad formula added 11/27
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

    # new graph added 11/27 
    import matplotlib.pyplot as plt 
    def graph():
        x = [1,2,3] 
        
        y = [2,4,1] 

        plt.plot(x, y) 
        plt.xlabel('x - axis') 
        plt.ylabel('y - axis') 
        plt.title('My first graph!') 
        plt.show()

    def degrees():
        celsius=float(input("Enter degree:"))
        fahrenheit = (celsius * 1.8) + 32
        print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

    def weight():
        pounds = float(input('Enter weight in Pounds(Lbs) to Convert into Kilograms:'))
        kilo_grams = pounds * 0.453592
        print(pounds,' Pounds (Lbs) are equal to', kilo_grams,'Kilograms (Kgs)')

    def multiplication():
      while(True):
        sum=1
        i=input('Enter the numbers separated by a space to be multiply: ')
        if(i=="finish"):
          a=180
          break
        try:
          l2=i.split()
          for s in range(len(l2)):
            sum*=int(l2[s])
          print('The product of those numbers are: ',sum)
          print()
          break
        except:
          print("Please enter numbers, try again.")
          print()
    def division():
      while(True):
        t=1
        i=input('Enter the numbers separated by a space to be divided: ')
        if(i=="finish"):
          a=180
          break
        try:
          l2=i.split()
          sum=int(l2[0])
          for s in range(1,len(l2)):
            if(l2[s]==0):
              t=0
              break
            sum/=int(l2[s])
          if(t==1):
            print('The product of those numbers are:',sum)
            print()
            break
        except:
          print("Please enter correct numbers, try again.")
          print()
    def Substraction():
      while(True):
        i=input('Enter the numbers separated by a space to be substracted: ')
        if(i=="finish"):
          a=180
          break
        try:
          l2=i.split()
          sum=int(l2[0])
          for s in range(1,len(l2)):
            sum-=int(l2[s])
          print('The product of those numbers are:',sum)
          print()
          break
        except:
          print("Please enter numbers, try again.")
          print()
    def randNum():
      import random
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

    from math import sqrt
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
  
    if(x=='1'):
      print(a)
      addition()
      print(a)
    elif(x=="3"):
      multiplication()
    elif(x=="4"):
      division() 
    elif(x=="2"):
      Substraction()
    elif(x=="5"):
      randNum()
    elif(x=="6"):
      trig()
    elif(x=="7"):
      root()
    elif(x=="8"):
      quad()
    elif(x=="9"):
      graph()
    elif(x=="10"):
      degrees()
    elif(x=="11"):
      weight()
    elif(x=="12"):
      molarity()
    elif(x=="13"):
      pyth()
    else:
      print("Sorry, I did not understand your choice, try again.")
  x=input(" \nChoose an operation\n1.Add\n2.Substraction\n3.Multiply\n4.Divide\n5.Random Number\n6.Trigonometry\n7.Roots\n8.Quadratic Fomrula\n9.Graph\n10.Degrees\n11.Weight\n12.Molarity\n13.Pythagorean\n(Enter'finish'to stop the calculator)\n\nChoice")
  if(x=="finish"):
    a=180
    break
  menu()