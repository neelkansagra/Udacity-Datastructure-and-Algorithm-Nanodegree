"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
call_time =dict()
for call in calls:
    if call[0] in call_time.keys():
       call_time[call[0]] += int(call[3])
    else:
       call_time[call[0]] = int(call[3])
    if call[1] in call_time.keys():
       call_time[call[1]] += int(call[3])
    else:
       call_time[call[1]] = int(call[3])

max_time = 0
max_number=''

for time in call_time:
    if call_time[time] >= max_time:
        max_time = call_time[time]
        max_number = time
print(max_number+" spent the longest time, "+str(max_time)+" seconds, on the phone during September 2016.")
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
