#!usr/bin/python


"""
This the class for fractions and fraction arithmetic
To be used instead of the list driven fractions module
Here the operators are overloaded to facilitate
fractional arithmetic.

In other words: addition and subtraction make use of
finding a common denominator.

e.g. 
    1/2 - 1/3 = 3/6 - 2/6 = 1/6

All results of operations are then reduced.
And if possible, fractions are reduced to integers.

e.g.
   7/8 + 1/8 = 1

the operations must be carried out with variables
so that integer division doesn't occur unecessarily.

But when you print the variable it will be represented as a/b.

e.g.
   a = Fraction(2,3)
   print a
----> 2/3
while just typing
   a
-----> <Fraction.Fraction instance at 0x5df5a8>

But all the operations work pretty well.
Enjoy 
"""
from math import floor, log

def makeFrac(num):
    return Fraction(num,1)

def makeInterval(num):
    import math
    if type(num)==int:
        return Interval(num, 2**int(math.floor(math.log(num,2))))
    else:
        return "Error!! Number must be an integer!"

class Fraction(object):


    def __init__(self, numer, denom):
         self.numer = numer
         self.denom = denom

    def gcd(self, numA, numB):
         if numB==0:
              return numA
         return self.gcd(numB, numA%numB)

    def lcm(self, numA, numB):
         return (numA*numB)/self.gcd(numA, numB)

    def reduce(self, numer, denom):
         if numer%denom == 0:
             return numer/denom
         reducedNumer = numer/self.gcd(numer, denom)
         reducedDenom = denom/self.gcd(numer, denom) 
         return Fraction(reducedNumer, reducedDenom)
   
    def makeNum(self):
         if self.numer%self.denom == 0:
             return self.numer/self.denom
         else:
             return (1.0*self.numer)/self.denom

    def __str__(self):
         return `self.numer`+"/"+`self.denom`

    def __add__(self, x):
        if type(x) == int:
            commonDenom = self.denom
            leftNumerator = self.numer
            rightNumerator = x*self.denom
        else:
            commonDenom = self.lcm(self.denom, x.denom)
            leftNumerator = self.numer*(commonDenom/self.denom)
            rightNumerator = x.numer*(commonDenom/x.denom)
        newNumerator = leftNumerator+rightNumerator
        return  self.reduce(newNumerator, commonDenom)         

    def __radd__(self, x):
        if type(x) == int:
            commonDenom = self.denom
            leftNumerator = self.numer
            rightNumerator = x*self.denom
        else:
            commonDenom = self.lcm(self.denom, x.denom)
            leftNumerator = self.numer*(commonDenom/self.denom)
            rightNumerator = x.numer*(commonDenom/x.denom)
        newNumerator = leftNumerator+rightNumerator
        return  self.reduce(newNumerator, commonDenom)


    def __sub__ (self, x):
        if type(x) == int:
            commonDenom = self.denom
            leftNumerator = self.numer
            rightNumerator = x*self.denom
        else:
            commonDenom = self.lcm(self.denom, x.denom)
            leftNumerator =self.numer*(commonDenom/self.denom)
            rightNumerator = x.numer*(commonDenom/x.denom)
        newNumerator = leftNumerator-rightNumerator
        return  self.reduce(newNumerator, commonDenom)

    def __rsub__(self, x):
        if type(x) == int:
            commonDenom = self.denom
            leftNumerator = self.numer
            rightNumerator = x*self.denom
        else:
            commonDenom = self.lcm(self.denom, x.denom)
            leftNumerator =self.numer*(commonDenom/self.denom)
            rightNumerator = x.numer*(commonDenom/x.denom)
        newNumerator = rightNumerator-leftNumerator
        return  self.reduce(newNumerator, commonDenom)
      

    def __mul__ (self, x):
        if type(x) == int:
            newNumer = self.numer*x
            newDenom = self.denom
        else:
            newNumer = self.numer*x.numer
            newDenom = self.denom*x.denom
        return  self.reduce(newNumer, newDenom)

    def __rmul__(self, x):
        if type(x) == int:
            newNumer = self.numer*x
            newDenom = self.denom
        else:
            newNumer = self.numer*x.numer
            newDenom = self.denom*x.denom
        return  self.reduce(newNumer, newDenom)

    def __div__ (self, x):
         if type(x)==int:
             newNumer = self.numer
             newDenom = self.denom*x
         else:
             newNumer = self.numer*x.denom
             newDenom = self.denom*x.numer
         return  self.reduce(newNumer, newDenom)

    def __rdiv__ (self, x):
         if type(x)==int:
             newNumer = self.denom*x
             newDenom = self.numer
         else:
             newNumer = self.denom*x.numer
             newDenom = self.numer*x.denom
         return  self.reduce(newNumer, newDenom)

    def __pow__ (self, x):
         newNumer = self.numer**x
         newDenom = self.denom**x
         if type(newNumer)==int and  type(newDenom)==int:
             return self.reduce(newNumer, newDenom)
         else:
             return newNumer/newDenom

    def __rpow__ (self, x):
        return pow(x,(1.0*self.numer)/self.denom)

    def __neg__ (self):
          return Fraction(self.numer*(-1),self.denom)

    def __lt__ (self, x):
        if type(x)==int:
            commonDenom = self.denom
            leftNumerator = self.numer
            rightNumerator = x*self.denom
        else:
            commonDenom = self.lcm(self.denom, x.denom)
            leftNumerator =self.numer*(commonDenom/self.denom)
            rightNumerator = x.numer*(commonDenom/x.denom)
        if leftNumerator < rightNumerator:
             return True
        else:
             return False

    def __le__ (self, x):
        if type(x)==int:
            commonDenom= self.denom
            leftNumerator = self.numer
            rightNumerator = x*self.denom
        else:
            commonDenom = self.lcm(self.denom, x.denom)
            leftNumerator =self.numer*(commonDenom/self.denom)
            rightNumerator = x.numer*(commonDenom/x.denom)
        if leftNumerator <= rightNumerator:
             return True
        else:
             return False

    def __gt__ (self, x):
        if type(x)==int:
            commonDenom= self.denom
            leftNumerator = self.numer
            rightNumerator = x*self.denom
        else:
            commonDenom = self.lcm(self.denom, x.denom)
            leftNumerator =self.numer*(commonDenom/self.denom)
            rightNumerator = x.numer*(commonDenom/x.denom)
        if leftNumerator > rightNumerator:
             return True
        else:
             return False

    def __ge__ (self, x):
        if type(x)==int:
            commonDenom= self.denom
            leftNumerator = self.numer
            rightNumerator = x*self.denom
        else:
            commonDenom = self.lcm(self.denom, x.denom)
            leftNumerator =self.numer*(commonDenom/self.denom)
            rightNumerator = x.numer*(commonDenom/x.denom)
        if leftNumerator >= rightNumerator:
             return True
        else:
             return False

    def __eq__ (self, x):
        if type(x)==int:
            commonDenom= self.denom
            leftNumerator = self.numer
            rightNumerator = x*self.denom
        else:
            commonDenom = self.lcm(self.denom, x.denom)
            leftNumerator =self.numer*(commonDenom/self.denom)
            rightNumerator = x.numer*(commonDenom/x.denom)
        if leftNumerator == rightNumerator:
             return True
        else:
             return False
 
    def __ne__ (self, x):
        if type(x)==int:
            commonDenom= self.denom
            leftNumerator = self.numer
            rightNumerator = x*self.denom
        else:
            commonDenom = self.lcm(self.denom, x.denom)
            leftNumerator =self.numer*(commonDenom/self.denom)
            rightNumerator = x.numer*(commonDenom/x.denom)
        if leftNumerator == rightNumerator:
             return False
        else:
             return True

         

