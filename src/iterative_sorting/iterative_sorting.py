# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        #loop through every int except the fist and compare to first int
            #if one is bigger than the first update smallest_index
        for j in range(i + 1, len(arr)):
            #why not len(arr)-1
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    #keep track of the len of arr
    list_size = len(arr)
    #loop through the arr while list size is > 1
    while list_size > 1:
        #loop again
        for i in range(0, list_size-1):
            #select the current index and compare to the next el
            #if curr el is larger swap places
            curr_index = i
            if arr[curr_index] > arr[i+1]:
                arr[curr_index], arr[i+1] = arr[i+1], arr[curr_index]
            #ignore the last el in the list and repeat
        list_size -= 1

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
