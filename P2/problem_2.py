import random
def rotated_array_search(input_list, number):
   """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
   """
   if len(input_list) == 0:
      return -1
   start = input_list[0]
   first = 0
   last = len(input_list) - 1
   if number == start:
       return 0
   while first<=last:
       mid = (first+last)//2
       if number<start and start <input_list[mid]:
           first = mid+1
       elif number<input_list[mid] and input_list[mid] <start:
           last = mid-1
       elif start<number and  number<input_list[mid]:
           last = mid-1
       elif start<input_list[mid] and  input_list[mid]<number:
           first = mid+1
       elif input_list[mid]<start and start <number:
           last = mid-1
       elif input_list[mid]<number and number <start:
           first = mid+1
       elif input_list[mid] == number:
           return mid
   return -1
   pass

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print(input_list)
        print(number)
        print("Fail")
        
if __name__ == '__main__':
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
    test_function([[3, 4, 5, 1, 2], 1])
    test_function([[1, 2, 3, 4, 5, 6], -1])
    test_function([[1, 2, 3, 4, 5, 6], 7])
    test_function([[], 7])
