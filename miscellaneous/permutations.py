def permute(s: str, answer: str, results: set):
    if not s:
        if answer not in results:
            print(answer, end=" ")
            results.add(answer)
        return None
    
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i+1:]
        rest = left_substr + right_substr
        permute(rest, answer+ch, results)

def swap(s, i, j):
    arr = list(s)
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return "".join(arr)

def backtrack_permute(s: str, left, right, results: set):
    if left == right:
        if s not in results:
            print(s, end=" ")
            results.add(s)
    else:
        for i in range(left, right+1):
            s = swap(s, left, i)
            backtrack_permute(s, left+1, right, results)
            s = swap(s, left, i)


s = input()
backtrack_permute(s, 0, len(s)-1, set())



