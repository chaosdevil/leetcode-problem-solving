import random
from time import time


def merge(l1, l2):
    return helper([], l1, l2)

def helper(merged, l1, l2):

    if not l1 and not l2:
        return merged

    if not l1 and l2:
        merged.append(l2.pop(0))
        return merged
    if l1 and not l2:
        merged.append(l1.pop(0))
        return merged

    if l1[0] <= l2[0]:
        merged.append(l1.pop(0))
        helper(merged, l1, l2)
    elif l1[0] > l2[0]:
        merged.append(l2.pop(0))
        helper(merged, l1, l2)

    return merged


if __name__ == "__main__":
    random.seed(123)
    l1 = sorted([random.randint(1,500) for _ in range(400)])
    l2 = sorted([random.randint(1,500) for _ in range(400)])

    start = time()
    merged_list = merge(l1, l2)
    print(merged_list)
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")
