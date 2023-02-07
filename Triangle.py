# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Feb. 6, 2023

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Jolene Ciccarone
"""
import math
from mybrand import my_brand
my_brand("SSW 567 HW 02a-Testing a legacy program and reporting on testing results")

def classifyTriangle(a,b,c):

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
      
    # Triangle Inequality Theorem
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly greater than the third side
    if not(((b + c) > a) and ((a + c) > b) and ((a + b) > c)):
        return 'NotATriangle'

    iso = False
    right = False
    # now we know that we have a valid triangle 
    if (math.isclose(a,b) and math.isclose(b,c) and math.isclose(a,c)):
        return 'Equilateral'
    if (math.isclose(a,b) or math.isclose(b,c) or math.isclose(a,c)):
        iso = True
    if (math.isclose(a**2 + b**2, c**2) or math.isclose(b**2 + c**2, a**2) or math.isclose(a**2 + c**2, b**2)):
        right = True
    if iso:
        if right:
            return "Isosceles and Right"
        else:
            return "Isosceles"
    else:
        if right:
            return "Scalene and Right"
        else:
            return "Scalene"

my_brand("SSW 567 HW 02a-Testing a legacy program and reporting on testing results")
