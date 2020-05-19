"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
telemark_num = []
call_senders = set([i[0] for i in calls])
call_receivers = set([i[1] for i in calls])
text_senders = set([i[0] for i in texts])
text_receivers = set([i[1] for i in texts])
for sender in call_senders:
    if(sender not in call_receivers and sender not in text_senders and sender not in text_receivers):
        telemark_num.append(sender)
telemark_num.sort()
print("These numbers could be telemarketers: ")
for i in telemark_num:
    print(i)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
