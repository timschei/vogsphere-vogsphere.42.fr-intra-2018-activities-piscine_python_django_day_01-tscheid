#!/usr/local/bin/python3

import sys

def	func(arg) :
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
						print (k2)
	else :
		print("Unknown City")

if __name__ == '__main__' :
    if len(sys.argv) == 2 :
        func(sys.argv[1])