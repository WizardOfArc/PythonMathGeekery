#!/usr/bin/python
import math

def gcd(a,b):
    if a==b:
        return a
    if a > b:
        return gcd(a-b, b)
    if a < b:
        return gcd(a, b-a)

def frac2fret(num,den):
    if num == den:
        return 0
    else:
        return -12*math.log(num*1.0/den, 2)

def reducedFrac(den):
    return [(s,den) for s in range(1,1+den) if gcd(s,den)==1]

def overtoneFrets(ot):
    fretList = []
    for frac in reducedFrac(ot):
        fretList.append(frac2fret(frac[0],frac[1]))
    return fretList




