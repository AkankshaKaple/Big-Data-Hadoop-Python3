#!/usr/bin/env python3
"""reducer code for average age of male and female die in titanic"""

import sys

count_sum_age = 0
count_total_male_traveler = 0
count_total_female_traveler = 0
traveler_gen = None
traveler = None
male_age_count = 0
female_age_count = 0


for line in sys.stdin:
	line = line.strip()
	traveler,count = line.split('\t',1)

	try:
		count = int(count)
	except:
		continue
	if  traveler == 'male':
		male_age_count += count
		count_total_male_traveler = count_total_male_traveler + 1
	elif  traveler == 'female':
		female_age_count += count
		count_total_female_traveler = count_total_female_traveler + 1


print("average age of female",int(female_age_count / count_total_female_traveler))
print("average age of male",int(male_age_count / count_total_male_traveler))
