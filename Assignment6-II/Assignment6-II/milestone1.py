"""
ID:0711506
Author:王偉誠
File: Milestone1.py
-----------------------
This file is to test the code for 
babyname.py milestone 1

"""
import sys


def add_data_for_name(name_data, year, rank, name):
	if name not in name_data:
		name_data[name] = {year: rank}
	elif name in name_data:
		if year in name_data[name]:
			if int(name_data[name][year]) > int(rank):
				name_data[name][year] = rank
		elif year not in name_data[name]:
			name_data[name][year] = rank
	pass

# ------------- DO NOT EDIT THE CODE BELOW THIS LINE ---------------- #


def test1():
	name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
	add_data_for_name(name_data, '2010', '208', 'Kate')
	print('--------------------test1----------------------')
	print(str(name_data))
	print('-----------------------------------------------')


def test2():
	name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}, 'Sammy': {'1990': '100'}}
	add_data_for_name(name_data, '1990', '200', 'Sammy')
	print('-------------------test2-----------------------')
	print(str(name_data))
	print('-----------------------------------------------')


def test3():
	name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
	add_data_for_name(name_data, '2000', '104', 'Kylie')
	print('--------------------test3----------------------')
	print(str(name_data))
	print('-----------------------------------------------')


def main():
	args = sys.argv[1:]
	if len(args) == 1 and args[0] == 'test1':
		test1()
	elif len(args) == 1 and args[0] == 'test2':
		test2()
	elif len(args) == 1 and args[0] == 'test3':
		test3()


if __name__ == "__main__":
	main()