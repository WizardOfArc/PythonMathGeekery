#!/usr/bin/python
"""This module and program is designed to find the nth fibonacci
   number. It also includes a function that will make a table
   and compare the nth Fibonacci number to phi**n.
"""
from math import sqrt

def findFib(n):
    fiboList = []
    for i in range(n):  #fill a list of n length with zeros
        fiboList.append(0)
    return fibo(n, fiboList)
    
def fibo(n, fiboList):
    if fiboList[n-1] != 0:
        return fiboList[n-1]
    else:
        if (n <= 2):
            fiboList[n-1] = 1
            return 1
        else:
            fiboList[n-1] = fibo(n-1, fiboList) + fibo(n-2, fiboList)
            return fiboList[n-1]

    
