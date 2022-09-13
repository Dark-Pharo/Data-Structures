def select(arr):
    
    for i in range(len(arr)):
        min_x = i 

        for item in range(i+1, len(arr)):
            if arr[item] < arr[min_x]:
                min_x = item

        arr[i], arr[min_x] = arr[min_x], arr[i]

arr = [20, 15, 12, 10, 2]
select(arr)

print(arr)