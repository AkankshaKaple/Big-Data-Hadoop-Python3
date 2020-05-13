#!/usr/env python3

"""code for survived people in titanic classvise"""

import sys

for line in sys.stdin:
	line = line.strip()
	traveler = line.split(",")
	if traveler[1] == '0':
		print('%s\t%s' % (traveler[2],1)) 
