# https://leetcode.com/problems/shortest-palindrome/

import os

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        reversed_s = s[::-1]
        
        # join s and reversed_s 
        # with @ as a mark to avoid overlapping
        joined_s = s + '@' + reversed_s
        
        # KMP table
        table = [0] * len(joined_s)
        
        for i in range(1, len(joined_s)):
            j = table[i-1]
            while j > 0 and joined_s[i] != joined_s[j]:
                j = table[j-1]
            if joined_s[i] == joined_s[j]:
                table[i] = j + 1
        return reversed_s[0:len(s)-table[len(joined_s)-1]] + s
            
        
if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/shortest_palindrome_testcase.txt", "r") as file:
        s = file.readline().strip()

    solution = Solution()
    print(solution.shortestPalindrome(s))