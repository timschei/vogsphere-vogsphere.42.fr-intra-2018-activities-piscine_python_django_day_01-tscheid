#!/usr/local/bin/python3

import sys

def	func(lis) :
	arg = " ".join(lis.title().split())
	states = {
		"Oregon"    : "OR",
		"Alabama"   : "AL",
		"New Jersey": "NJ",
		"Colorado"  : "CO"
        }

	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
        }
	if arg in capital_cities.values():
		for k, v in capital_cities.items():
			if arg == v :
				for k2, v2 in states.items():
					if k == v2 :
						print (arg," is the capital city of ", k2)
	elif arg in states :
		print(capital_cities[states[arg]]," is the capital city of ", arg)
	else:
		print(arg," is neither a capital city nor a state")

if __name__ == '__main__' :
    if len(sys.argv) == 2 :
        tab = sys.argv[1].split(',')
        for v0 in range(len(tab)):
        	if len(tab[v0].strip()) > 0:
        		func(tab[v0].strip())