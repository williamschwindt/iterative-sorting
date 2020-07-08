def linear_search(arr, target):
    for el in arr:
        if el == target:
            return arr.index(el)


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #keep track of start and end
    start = 0
    end = len(arr)-1

    #loop through until target is found or end = start
    while end >= start:
        #find the middle
        middle = (start + end) // 2
        #if the middle is the target return 
        if arr[middle] == target:
            return middle
        #if the target is greater then the middle ignore the left side
        elif target > arr[middle]:
            start = middle + 1
        #if the target is less then the middle ignore the right side
        elif target < arr[middle]:
            end = middle - 1

    return -1  # not found
