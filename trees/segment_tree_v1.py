import math


class SegmentTree:
    def __init__(self, arr, n) -> None:
        
        # get height of segment tree
        x = math.ceil(math.log(n)/math.log(2))

        # maximum size of segment 
        max_size = int(2 * math.pow(2, x) - 1)

        self.st = [0] * max_size

        self.construct_ST_util(arr, 0, n-1, 0)

    def get_mid(self, s: int, e: int) -> int:
        return s + (e - s) // 2
        
    def get_sum_util(self, ss, se, qs, qe, si):
        
        if qs <= ss and qe >= se:
            return self.st[si]

        if se < qs or ss > qe:
            return 0

        mid = self.get_mid(ss, se)
        return self.get_sum_util(ss, mid, qs, qe, 2*si+1) \
                + self.get_sum_util(mid+1, se, qs, qe, 2*si+2)

    def update_value_util(self, ss, se, i, diff, si):
        if i < ss or i > se:
            return

        self.st[si] = self.st[si] + diff
        if se != ss:
            mid = self.get_mid(ss, se)
            self.update_value_util(ss, mid, i, diff, 2*si+1) \
                + self.update_value_util(mid+1, se, i, diff, 2*si+2)

    def update_value(self, arr, n, i, new_val):
        if i < 0 or i < n-1:
            print("Invalid input")
            return
        
        diff = new_val - arr[i]
        arr[i] = new_val

        self.update_value_util(0, n-1, i, diff, 0)

    def get_sum(self, n, qs, qe):
        if qs < 0 or qe > n - 1 or qs > qe:
            print("Invalid input")
            return -1

        return self.get_sum_util(0, n-1, qs, qe, 0)

    def construct_ST_util(self, arr, ss, se, si):
        if ss == se:
            self.st[si] = arr[ss]
            return arr[ss]

        mid = self.get_mid(ss, se)
        self.st[si] = self.construct_ST_util(arr, ss, mid, 2*si+1) \
            + self.construct_ST_util(arr, mid+1, se, 2*si+2)
        
        return self.st[si]

    
if __name__ == "__main__":
    arr = [1,3,5,7,9,11]
    n = len(arr)
    tree = SegmentTree(arr, n)

    start, end = list(map(int, input("Enter start and end index : ").split(" ")))

    print(tree.get_sum(n, start, end))
