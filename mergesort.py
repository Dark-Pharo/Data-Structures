def mergesort(my_array):
    if len(my_array) == 1:
        return my_array

    mid = len(my_array) // 2
    left = my_array[:mid]
    right = my_array[mid:]

    left_result = mergesort(left)
    right_result = mergesort(right)

    return merge(left_result, right_result)

def merge(left_result, right_result):
    result = [None] * (len(left_result) + len(right_result))
    i = j = k = 0

    while i < len(left_result) and j < len(right_result):
        if left_result[i] <= right_result[j]:
            result[k] = left_result[i]
            i += 1
        else:
            result[k] = right_result[j]
            j += 1
        k += 1

    while i < len(left_result):
        result[k] = left_result[i]
        i += 1
        k += 1

    while j < len(right_result):
        result[k] = right_result[j]
        j += 1
        k += 1

    return result

numbers = [4, 5, 6, 1, 3, 7, 2]
print(mergesort(numbers))