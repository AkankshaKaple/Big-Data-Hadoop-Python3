REGISTER '/home/akanksha/Akanksha/Big_Data/Apache_Pig/udfs/my_udf.py' USING streaming_python AS my_udfs_obj;
data = LOAD '/home/hduser/Pig/CPU_logs/input/Processed_cpu_logs.csv' USING PigStorage(',') as (date_time:datetime, user:chararray, mouse:int, keyboard:int);
grouped_user = GROUP data BY user;
describe grouped_user;
users = FOREACH grouped_user GENERATE my_udfs_obj.process_user(data);
STORE users INTO '/home/hduser/Pig/CPU_logs/input/output_1';
