from pyhive import hive
import pandas as pd
host_name = "localhost"
port = 10000
user = "hduser"
password = "Admin@123"
database="user_log"

conn = hive.Connection(host='localhost', port=port, auth='NOSASL', database='user_log')
hive_df = pd.read_sql("SELECT username,idle_time FROM user_log_data2", conn)
#user with most idele_time 
 
avg_hour_df  = pd.read_sql("SELECT username,working_hour FROM user_log_data2",conn)
#avg_hour_df['working_hour'] = pd.to_datetime(avg_hour_df['working_hour'], format="%d days %H%M%S")
#avg_hour_df.to_timestamp(avg_hour_df.working_hour)
#print(avg_hour_df['working_hour'].dtype)
avg_hour_df['working_hour']=avg_hour_df['working_hour'].replace("0 days","")
avg_hour_df['working_hour']=pd.to_datetime(avg_hour_df['working_hour']
print(avg_
