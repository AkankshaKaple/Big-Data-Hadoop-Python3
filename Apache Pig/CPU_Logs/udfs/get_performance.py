import datetime
from my_pig_util import outputSchema
import pandas as pd


@outputSchema('value:chararray')
def process_user(data):
   data = pd.DataFrame(data, columns=['DateTime', 'user_name', 'mouse', 'keyboard'])
   data['Dates'] = pd.to_datetime(data['DateTime']).dt.date
   data['Time'] = pd.to_datetime(data['DateTime']).dt.time
   date = data['Dates'].unique()[0]
   user = data['user_name'].unique()[0]
   start = min(data.Time)
   end = max(data.Time)
   starthours = datetime.datetime.combine(date, start)
   endhours = datetime.datetime.combine(date, end)
   diff = (endhours - starthours)
   diff = diff.seconds / 3600
   json_data = {}
   for i in range(len(data)):
      if str(end) in str(data['DateTime'].iloc[i]):
         json_data['end'] = data['DateTime'][i]
      if str(start) in str(data['DateTime'].iloc[i]):
         json_data['start'] = data['DateTime'][i]

   json_data["user"] = user

   idle_hours = (datetime.datetime.combine(data['Dates'][0], start) - datetime.datetime.combine(data['Dates'][0],
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

   json_data["idle_hours"] = idle_hours
   json_data["average_working_hours"] = diff - json_data["idle_hours"]

   z = pd.DataFrame([json_data])
   return z
