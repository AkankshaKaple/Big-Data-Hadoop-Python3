#!/usr/bin/python3
""" reducer code to find survived traveler classvised in titanic"""

import sys

classvise_count = 0
first_class_survived = 0
second_class_survived = 0
third_class_survived = 0


for line in sys.stdin:
	line = line.strip()
	traveler,count = line.split('\t',1)
	if traveler == '1':
		first_class_survived = first_class_survived + 1
	elif traveler == '2':
		second_class_survived = second_class_survived +1
	elif traveler == '3':
		third_class_survived = third_class_survived +1

print("First class survived",first_class_survived)
print("second class survived",second_class_survived)
print("third class survived",third_class_survived)
