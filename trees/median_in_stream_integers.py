def binary_search(arr, item, low, high):
    if low >= high:
        return (low+1) if item > arr[low] else low

    # find middle
    mid = low + (high-low) // 2

    if item == arr[mid]:
        return mid + 1
    if item > arr[mid]:
        return binary_search(arr, item, mid+1, high)
    
    return binary_search(arr, item, low, mid-1)

def print_median(arr, n):
    count = 1
    j = 0
    print(f"median after reading 1 element is {arr[0]}")
    for i in range(1, n):
        j = i - 1
        num = arr[i]

        position = binary_search(arr, num, 0, j)

        while j >= position:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = num
        count += 1

        if count % 2 != 0:
            median = arr[count // 2]
        else:
            median = (arr[(count//2) - 1] + arr[count//2]) // 2

        print(f"median after reading {i+1} element is {median}")


arr = list(map(int, input().split(" ")))

print_median(arr, len(arr))
