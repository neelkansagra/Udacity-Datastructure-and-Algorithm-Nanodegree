def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    first = 0
    last = number
    while first <=last:
        mid = (first+last)//2
        if mid*mid > number:
            last = mid-1
        elif mid*mid <number:
            first = mid+1
        else:
           return mid
    return first-1
    pass

if __name__ == '__main__':
    print("Pass" if (-1 == sqrt(-120)) else "Fail")
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
    print("Pass" if (31 == sqrt(999)) else "Fail")
    print("Pass" if (92 == sqrt(8572)) else "Fail")
    print("Pass" if (436 == sqrt(190292)) else "Fail")
