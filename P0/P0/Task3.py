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

def area_code(call):
    received_call = call[1]
    area_code = ''
    if received_call[:3] == '140':
       area_code = received_call[:3]
    elif received_call[:2] == '(0':
        for i in received_call:
            area_code +=i
            if i==')':
                break
    else:
        area_code = received_call[:4]
    return area_code
bng_area_code=[]
for call in calls:
    if call[0][0:5] == '(080)':
        bng_area_code.append(area_code(call))
bng_area_code_list = list(set(bng_area_code))
bng_area_code_list.sort()
print("\n The numbers called by people in Bangalore have codes:")
for code in bng_area_code_list:
    print(code)
count_bng_calls = 0
for code in bng_area_code:
    if code == '(080)':
        count_bng_calls+=1
print(str(round(count_bng_calls/len(bng_area_code)*100, 2))+ " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
















