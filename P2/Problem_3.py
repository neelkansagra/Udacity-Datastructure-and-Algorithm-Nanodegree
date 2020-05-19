def mergesort(items):

    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):

    arr = left+right
    merged = []
    left_index = 0
    right_index = 0

   
    while left_index < len(left) and right_index < len(right):
        
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
       
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

   
    return merged

def is_digits(input_list):
    """
    Check if the elements in the array are integer digits between 0 to 9.
    Args:
       input_list(list): Input List
    Returns:
       (bool): True if all integers are non negative numbers
    """

    for i in range(0,len(input_list)):
        item = input_list[i]
        if type(item) != int or item < 0 or item > 9:
            return False
    return True

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    
    if len(input_list) <= 1 or input_list is None or not is_digits(input_list):
        return -1,-1

    
    arr_sorted = mergesort(input_list)
    arr_sorted.reverse()
    last_index = len(arr_sorted) - 1

    
    num1, num2, exp = 0, 0, 0

    
    for i in range(0,len(arr_sorted),2):
        if i <= last_index: 
            num1 = num1*10 + arr_sorted[i]
        if (i+1) <= last_index: 
            num2 = num2*10 + arr_sorted[i+1]
        exp += 1

    return num1, num2

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        return "Pass"
    else:
        return "Fail"




arr = [1, 2, 3, 4, 5]
sol = [542, 31]
test = test_function([arr, sol])
print('rearrange_digits({}): \t{} \t {}'.format(arr, sol, test))


arr = [4, 6, 2, 5, 9, 8]
sol = [964, 852]
test = test_function([arr, sol])
print('rearrange_digits({}): \t{} \t {}'.format(arr, sol, test))


arr = [None] # Null input
sol = [-1, -1]
test = test_function([arr, sol])
print('rearrange_digits({}): \t{} \t {}'.format(arr, sol, test))

arr = [] # Empty input
test = test_function([arr, sol])
print('rearrange_digits({}):   \t{} \t {}'.format(arr, sol, test))

arr = [0] # Single value
test = test_function([arr, sol])
print('rearrange_digits({}):  \t{} \t {}'.format(arr, sol, test))

arr = [1, -2] # negative value
test = test_function([arr, sol])
print('rearrange_digits({}):  \t{} \t {}'.format(arr, sol, test))

arr = [1, 10] # two digits
test = test_function([arr, sol])
print('rearrange_digits({}):  \t{} \t {}'.format(arr, sol, test))

arr = [1, 2.5] # float value
test = test_function([arr, sol])
print('rearrange_digits({}):  \t{} \t {}'.format(arr, sol, test))


arr = [5,5,0,5,5,4] # duplictes value
sol = [550, 554]
test = test_function([arr, sol])
print('rearrange_digits({}): \t{} \t {}'.format(arr, sol, test))

arr = [1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1] # duplictes value
sol = [987654321, 987654321]
test = test_function([arr, sol])
print('rearrange_digits({}): \t{} \t {}'.format(arr, sol, test))
