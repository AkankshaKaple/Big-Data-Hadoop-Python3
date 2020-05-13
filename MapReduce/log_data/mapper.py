import sys
import pandas as pd
import datetime

datetime_list = []
user_name_list = []
mouse_list = []
tech_list = []
keyboard_list = []
count = 0
for line in sys.stdin:
    if count != 0:
        line = line.strip()
        DateTime, username, Keyboard, Mouse, Technology = line.split(',')

        datetime_list.append(DateTime)
        user_name_list.append(username)
        mouse_list.append(Mouse)
        tech_list.append(Technology)
        keyboard_list.append(Keyboard)
    count+=1

data = pd.DataFrame({'DateTime': datetime_list, 'user_name': user_name_list, 'keyboard': keyboard_list
                     , 'technology': tech_list, 'mouse': mouse_list})
data['Dates'] = pd.to_datetime(data['DateTime']).dt.date
data['Time'] = pd.to_datetime(data['DateTime']).dt.time

def idle_hours(data, user):
    start = min(data.Time[(data.user_name == user)])
    idle_hours = (datetime.datetime.combine(date, start) - datetime.datetime.combine(date,
                                                                                     datetime.time(8, 30, 0))) / 3600
    idle_hours = idle_hours.seconds
    count = 0
    zero = 0
    for i in range(0, data.shape[0]):

        if (count == 5) and (zero == 5):
            idle_hours += 0.5
            count = 0
            zero = 0
        elif (count == 5) and (zero != 5):
            count = 0
            zero = 0

        if data.iloc[i]["keyboard"] == 0 and data.iloc[i]["mouse"] == 0:
            zero = zero + 1
        count = count + 1
    return idle_hours


for date in data['Dates'].unique():
    for user in data[data['Dates'] == date]['user_name'].unique():
        start = min(data.Time[(data.Dates == date) & (data.user_name == user)])
        end = max(data.Time[(data.Dates == date) & (data.user_name == user)])
        tech = data.technology[data.user_name == user].unique()[0]
        starthours = datetime.datetime.combine(date, start)
        endhours = datetime.datetime.combine(date, end)
        diff = (endhours - starthours)
        diff = diff.seconds / 3600
        json_data = {}
        avg_working_hr = diff - idle_hours(data[data.user_name == user], user)
        print(user, '\t', avg_working_hr)
