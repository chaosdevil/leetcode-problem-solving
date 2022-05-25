# https://leetcode.com/problems/longest-valid-parentheses/solution/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # plan : dynamic programming
        max_length = 0
        dp = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1] >= 2 else 0) + 2
                    max_length = max(max_length, dp[i])
        # print(dp)
        return max_length


if __name__ == "__main__":
    s = "())((())"

    solution = Solution()
    print(solution.longestValidParentheses(s))