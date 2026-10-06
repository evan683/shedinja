#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2
import math
print("two step algebra equation ax + b = c")
a = float(input("what is the value of a "))
b = float(input("what is the value of b "))
c = float(input("what is the value of c "))

step_one = c - b
x = step_one / a
print(f"x equals {x:.0f}")