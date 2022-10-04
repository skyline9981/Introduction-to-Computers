"""
File: rocket.py
ID:0711506
author:WEI-CHENG, Wang
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""


SIZE = 3
# You can change the size of rocket here.

def main():
	"""
	You can use this program to print a rocket for any size.
	Like:
	   /\
	  //\\
	 ///\\\
	+======+
	|../\..|
	|./\/\.|
	|/\/\/\|
	|\/\/\/|
	|.\/\/.|
	|..\/..|
	+======+
	   /\
	  //\\
	 ///\\\
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()

def head():
	"""
	Use some for_loops to print the head of the rocket.
	Like:
	  /\
	 //\\
	///\\\
	"""
	for i in range(SIZE):
		for J in range(SIZE-i):
			print(' ', end='')
		for j in range(i+1):
			print('/', end='')
		for j in range(i+1):
			print('\\', end='')
		print(' ')

def belt():
	"""
	Use some for_loops to print the belt of the rocket.
	Like:
	+======+
	"""
	print('+', end='')
	for i in range(SIZE):
		print('=', end='')
		print('=', end='')
	print('+')

def upper():
	"""
	Use some for_loops to print the upper of the rocket.
	Like:
	|../\..|
	|./\/\.|
	|/\/\/\|
	"""
	for i in range(SIZE):
		print('|', end='')
		for j in range(SIZE-i-1):
			print('.', end='')
		for j in range(i+1):
			print('/', end='')
			print('\\', end='')
		for j in range(SIZE - i - 1):
			print('.' , end='')
		print('|')

def lower():
	"""
	Use some for_loops to print the lower of the rocket.
	Like:
	|\/\/\/|
	|.\/\/.|
	|..\/..|
	"""
	for i in range(SIZE):
		print('|', end='')
		for j in range(i):
			print('.', end='')
		for j in range(SIZE-i):
			print('\\', end='')
			print('/', end='')
		for j in range(i):
			print('.', end='')
		print('|')




###### DO NOT EDIT CODE BELOW THIS LINE #####

if __name__ == '__main__':
	main()
