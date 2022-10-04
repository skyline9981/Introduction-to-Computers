"""
File: quadratic_solver.py
ID:0711506
author:WEI-CHENG, Wang
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	You can use this program to find out the roots of a equation like ax^2+bx+c=0.
	"""
	pass
	print('stanCode Quadratic Solver!')
	print('Enter a:', end='')
	a = int(input())
	print('Enter b:', end='')
	b = int(input())
	print('Enter c:', end='')
	c = int(input())
	D = b*b-4*a*c
	if D > 0:
		root1 = (-b + math.sqrt(D)) / 2 / a
		root2 = (-b - math.sqrt(D)) / 2 / a
		print('Two roots:', root1, ',', root2)
	elif D == 0:
		root3 = (-b + math.sqrt(D)) / 2 / a
		print('One root:', root3)
	elif D < 0:
		print('No real roots')

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
