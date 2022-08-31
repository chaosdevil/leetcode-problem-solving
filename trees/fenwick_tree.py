class FenwickTree:
    
    def __init__(self, arr, n) -> None:
        self.tree = [0] * (n+1)
        self.n = n
        for i in range(self.n):
            self.update(self.n, i, arr[i])
    
    def update(self, n, i, v):
        i += 1
        while i <= n:
            self.tree[i] += v
            i += i & (-i)

    def get_sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    
if __name__ == "__main__":
    arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(arr)
    bit = FenwickTree(arr, n)
    print(bit.tree)
    p = 7
    print(f"Sum of elements in arr[0..{p}] is " + str(bit.get_sum(p)))