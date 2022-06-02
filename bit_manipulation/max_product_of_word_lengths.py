from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        if not words:
            return 0
        n = len(words)
        val = [0 for _ in range(n)]
        for i in range(n):
            tmp = words[i]
            for j in range(len(tmp)):
                val[i] |= 1 << (ord(tmp[j]) - ord('a'))
        print(val)
        max_product = 0
        for i in range(n):
            for j in range(i+1, n):
                if (val[i] & val[j]) == 0:
                    max_product = max((len(words[i]) * len(words[j])), max_product)
        return max_product


if __name__ == "__main__":
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    solution = Solution()
    print(solution.maxProduct(words))