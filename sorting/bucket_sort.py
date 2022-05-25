# Python program for the above approach
# Bucket sort for numbers
# having integer part
from ast import literal_eval
from time import time


def bucketSort(arr, noOfBuckets):
    max_ele = max(arr)
    min_ele = min(arr)

    # range(for buckets)
    rnge = (max_ele - min_ele) / noOfBuckets

    temp = []

    # create empty buckets
    for i in range(noOfBuckets):
        temp.append([])

    # scatter the array elements
    # into the correct bucket
    for i in range(len(arr)):
        diff = (arr[i] - min_ele) / rnge - \
            int((arr[i] - min_ele) / rnge)

        # append the boundary elements to the lower array
        if(diff == 0 and arr[i] != min_ele):
            temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])

        else:
            temp[int((arr[i] - min_ele) / rnge)].append(arr[i])

    # Sort each bucket individually
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()

    # Gather sorted elements
    # to the original array
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                arr[k] = i
                k = k+1


# Driver Code
with open(r"C:\Users\yoksu\Desktop\algorithms\miscellaneous\contains_duplicate.txt", "r") as file:
    input = literal_eval(file.readline().strip())

arr = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0,
       8.0, 4.8, 7.68, -6.5, -5.4, 3.4, -6.35, 4.56, -8.75, 3.54, 1.24, -7.14, -3.56]
noOfBuckets = len(input) // 2
start = time()
bucketSort(input, noOfBuckets)
print("Sorted array: ", input)
print(f"Time elapsed : {(time() - start) * 1000} milliseconds")

# This code is contributed by
# Vinita Yadav
