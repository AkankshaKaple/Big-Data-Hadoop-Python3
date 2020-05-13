#!/usr/bin/env python3

"""program for average age of male and female died in titanic"""

import sys

#input comes from STDIN (standard input)
for line in sys.stdin:
	line = line.strip()
	traveler = line.split(",")
	if traveler[1] == "1":
		try:
			int(traveler[5])
			print('%s\t%s' % (traveler[4],traveler[5]))
		except:
			continue
		
