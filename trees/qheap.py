import heapq
from collections import defaultdict
from time import time

operations = []
with open("trees/testcases/qheap_input.txt", "r") as file:
    n = int(file.readline().strip())
    for _ in range(n):
        operations.append(file.readline().rstrip().split(" "))


# solve problem
class MinHeap:
    def __init__(self):
        self.n = 0
        self.heap_arr = [0 for _ in range(100000+1)]

    def min_heapify(self, i):
        left = 2 * i
        right = (2 * i) + 1
        minimum = i
        if left < self.n and self.heap_arr[left] < self.heap_arr[minimum]:
            minimum = left
        if right < self.n and self.heap_arr[right] < self.heap_arr[minimum]:
            minimum = right
        if minimum != i:
            self.swap(i, minimum)
            self.min_heapify(minimum)

    def swap(self, a, b):
        temp = self.heap_arr[a]
        self.heap_arr[a] = self.heap_arr[b]
        self.heap_arr[b] = temp

    def insert(self, k):
        if self.n == len(self.heap_arr):
            return None

        self.n += 1
        self.heap_arr[self.n] = k
        p = self.n

        while p > 1:
            pr = p // 2
            if self.heap_arr[pr] > self.heap_arr[p]:
                self.swap(pr, p)
                p = pr
            else:
                break

    def search(self, k):
        for i in range(1, self.n + 1):
            if self.heap_arr[i] == k:
                return i
        return -1

    def delete_key(self, k):
        index = self.search(k)
        self.heap_arr[index] = self.heap_arr[self.n]
        self.n -= 1
        self.min_heapify(index)

    def get_min(self):
        if self.n == 0:
            return -1
        else:       
            return self.heap_arr[1]


if __name__ == "__main__":
    start = time()
    minheap = MinHeap()
    result = []
    for opt in operations:
        if opt[0] == '1':
            minheap.insert(int(opt[1]))
        elif opt[0] == '2':
            minheap.delete_key(int(opt[1]))
        else:
            result.append(minheap.get_min())

    # print("\n".join(map(str, result)))
    print(len(result))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")
