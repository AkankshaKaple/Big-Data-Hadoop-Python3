import sys
import pandas as pd
user_name=[]
avg_working_hr=[]
curr_hr=0
curr_name = None
avg = []
for line in sys.stdin:
	line = line.strip()
	name, avg_hr = line.split('\t')
	user_name.append(name)
	avg_working_hr.append(float(avg_hr))

data = pd.DataFrame({'user_name': user_name, 'avg_working_hours': avg_working_hr})
for name in data.user_name.unique():
	df = data[data['user_name'] == name]['avg_working_hours']
	avg.append(sum(df) / len(df))

lowers_avg_hours = min(avg)
highest_avg_hours = max(avg)
print('Lowest number of average hours : {}'.format(lowers_avg_hours))
print('Highest number of average hours : {}'.format(highest_avg_hours))
