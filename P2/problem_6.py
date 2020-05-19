import random 
def get_min_max(ints):
    maxx = -1*float('inf')
    minn = float('inf')
    if ints:
        for i in ints:
            if i> maxx:
               maxx = i
            if i<minn:
               minn =i
    return (minn,maxx)

if __name__ == '__main__':
    test1 = [i for i in range(0, 10)]
    random.shuffle(test1)
    print("Pass" if ((0, 9) == get_min_max(test1)) else "Fail")

    test2 = [i for i in range(0, 100)]
    random.shuffle(test2)
    print("Pass" if ((0, 99) == get_min_max(test2)) else "Fail")

    test3 = [i for i in range(0, 1000)]
    random.shuffle(test3)
    print("Pass" if ((0, 999) == get_min_max(test3)) else "Fail")

    # Edge cases
    print("Pass" if ((-9, 0) == get_min_max([i for i in range(0, -10, -1)])) else "Fail")
    print("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
    print("Pass" if ((float('inf'), float('-inf')) == get_min_max([])) else "Fail")
    print("Pass" if ((float('inf'), float('-inf')) == get_min_max(None)) else "Fail")
    print("Pass" if ((-100, 99) == get_min_max([i for i in range(-100, 100)])) else "Fail")

