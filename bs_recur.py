def binarysearch(my_array, target):
    left = 0
    right = len(my_array)-1
    result = helper(my_array, target, left, right)
    return result

def helper(my_array, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    mid_element = my_array[mid]

    if target == mid_element:
        return mid
    elif target < mid_element:
        right = mid -1
        result = helper(my_array, target, left, right)
        return result
    else:
        left = mid + 1
        result = helper(my_array, target, left, right)
        return result