from ast import literal_eval

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for c in s:
            if stack and stack[-1][1] >= k:
                for _ in range(k):
                    stack.pop()
                if stack and c == stack[-1][0]:
                    stack.append((c, stack[-1][1]+1))
                else:
                    stack.append((c, 1))
            elif not stack or stack[-1][0] != c:
                pair = (c, 1)
                stack.append(pair)
            elif stack[-1][0] == c and stack[-1][1] < k:
                pair = (c, stack[-1][1]+1)
                stack.append(pair)

        if stack[-1][1] >= k:
            for _ in range(k):
                stack.pop()
            
        return "".join([pair[0] for pair in stack])


solution = Solution()
inp = literal_eval(input())
k = int(input())
print(solution.removeDuplicates(inp, k))