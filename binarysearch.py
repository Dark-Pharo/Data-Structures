def binarysearch(my_array, target):
    left = 0
    right = len(my_array)-1

    while left <= right:
        mid = (left + right) // 2
        mid_element = my_array[mid]

        if target == mid_element:
            return mid
        elif target < mid_element:
            right = mid -1
        else:
            left = mid + 1

    return -1

print(binarysearch([1, 5, 10, 12, 25, 30, 32], 29))