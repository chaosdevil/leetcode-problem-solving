from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def backtrack(s, current, idx, result):
            if len(current) == len(s):
                return
            
            sub = []
            for i in range(idx, len(s)):
                current = current + s[i]
                backtrack(s, current, idx+1, result)
                if is_palindrome(current):
                    sub.append(current)
                current = current[0:-1]
            if sub:
                result.append(sub[:])
            
            return
                
        def is_palindrome(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
                
        backtrack(s, "", 0, result)
        return result


if __name__ == "__main__":
    s = "aab"
    solution = Solution()
    print(solution.partition(s))