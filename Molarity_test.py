def main_molarity(grams, molMass, volume):
    volume = volume/1000
    molarity = grams/molMass/volume
    return molarity

def molarity():
    grams = float(input("Enter grams of substance: "))
    molMass = float(input("Enter molar mass of substance in grams per mole: "))
    volume = float(input("Enter volume in milliliters: "))
    print("The molarity of your solution is: ", 
          format(main_molarity(grams, molMass, volume),'.2f'), " mol/L.")

molarity()