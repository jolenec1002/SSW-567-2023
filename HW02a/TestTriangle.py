# -*- coding: utf-8 -*-
"""
Updated Feb. 6, 2023
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Jolene Ciccarone
"""

import unittest
import math

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework
from mybrand import my_brand
my_brand("SSW 567 HW 02a-Testing a legacy program and reporting on testing results")

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testScaRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Scalene and Right')

    def testScaRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,12,13),'Scalene and Right')
        
    def testEqualTriangleA(self): 
        self.assertEqual(classifyTriangle(6,6,6),'Equilateral')

    def testEqualTriangleB(self): 
        self.assertEqual(classifyTriangle(56,56,56),'Equilateral')
    
    def testEqualTriangleC(self): 
        self.assertEqual(classifyTriangle(5.3,5.3,5.3),'Equilateral')

    def testIsoTriangleA(self): 
        self.assertEqual(classifyTriangle(4,4,6),'Isosceles')

    def testIsoTriangleB(self): 
        self.assertEqual(classifyTriangle(46,46,25),'Isosceles')

    def testIsoTriangleC(self): 
        self.assertEqual(classifyTriangle(1.23,1.23,2),'Isosceles')

    def testIsoRightA(self): 
        self.assertEqual(classifyTriangle(2,2,math.sqrt(8)),'Isosceles and Right')

    def testIsoRightB(self): 
        self.assertEqual(classifyTriangle(3,3,math.sqrt(18)),'Isosceles and Right')

    def testScaTriangleA(self): 
        self.assertEqual(classifyTriangle(7,10,14),'Scalene')

    def testScaTriangleB(self): 
        self.assertEqual(classifyTriangle(15,13,20),'Scalene')

    def testScaTriangleC(self): 
        self.assertEqual(classifyTriangle(3.56, 7.2, 4),'Scalene')

    def testZeroInputA(self): 
        self.assertEqual(classifyTriangle(0,1,2),'InvalidInput')

    def testZeroInputB(self): 
        self.assertEqual(classifyTriangle(1,0,2),'InvalidInput')

    def testZeroInputC(self): 
        self.assertEqual(classifyTriangle(2,1,0),'InvalidInput')

    def testLargeInputA(self): 
        self.assertEqual(classifyTriangle(201,100,150),'InvalidInput')

    def testLargeInputB(self): 
        self.assertEqual(classifyTriangle(100,201,150),'InvalidInput')

    def testLargeInputC(self): 
        self.assertEqual(classifyTriangle(100,150,201),'InvalidInput')

    def testNotTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,2),'NotATriangle')

    def testNotTriangleB(self): 
        self.assertEqual(classifyTriangle(5,6,13),'NotATriangle')

    def testOrderA(self): 
        self.assertEqual(classifyTriangle(5,4,3),'Scalene and Right')

    def testOrderB(self): 
        self.assertEqual(classifyTriangle(12,13,5),'Scalene and Right')

    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

