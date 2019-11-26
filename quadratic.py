import cmath
 
class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def discriminant(self):
        return ((self.b)**2) - (4 * self.a * self.c)

    def root1(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.b + cmath.sqrt(self.discriminant())) / (2 * self.a)
    def root2(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.b - cmath.sqrt(self.discriminant())) / (2 * self.a)


#test = QuadraticEquation(1,5,6)
#print('The solution are {0} and {1}'.format(test.root1(),test.root2()))

 