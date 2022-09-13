def linearsearch(my_array, target):
    for i in range(len(my_array)):
        if my_array[i] == target:
            return i

    return -1

linearsearch([5,3,19,2], 9)