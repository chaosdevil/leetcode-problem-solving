from time import time

def isBalanced(s):
    stack = []
    opens = ['(', '{', '[']
    closes = [')', '}', ']']
    for ch in s:
        if ch in opens:
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack[-1]
            if opens.index(top) == closes.index(ch):
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


if __name__ == "__main__":
    with open("stacks-and-queues/balanced_parentheses_input.txt", "r") as file:
        t = int(file.readline().strip())
        start = time()
        for t_itr in range(t):
            s = file.readline().strip()

            result = isBalanced(s)

            print(result)
        print(f"Time Elapsed : {(time() - start) * 1000} milliseconds")
