#
# Title: skelton_calculator.py
# Author: Cody Skelton
# Date: 01.28.2024
# Purpose: Basic calculator app 
# Requirements from WEB 335 Exercise 3.3
#

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

num1 = 4
num2 = 4
num3 = add(num1, num2)

# Must typecast to string to allow concatenation
outputString = str(num1) + " + " + str(num2) + " is " + str(num3)
print(outputString)

# Python allows you to overwrite variables, so we'll reuse them
num1 = 10
num2 = 6
num3 = subtract(num1, num2)

outputString = str(num1) + " - " + str(num2) + " is " + str(num3)
print(outputString)

num1 = 8
num2 = 2
num3 = divide(num1, num2)

outputString = str(num1) + " / " + str(num2) + " is " + str(num3)
print(outputString)

num1 = 10
num2 = 2
num3 = multiply(num1, num2)

outputString = str(num1) + " * " + str(num2) + " is " + str(num3)
print(outputString)