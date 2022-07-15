# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
import os

from ast import literal_eval
from time import time
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # slow
        n = len(cardPoints)
        total_points = sum(cardPoints)
        skip = n - k
        max_points = 0
        i = 0
        while i <= n - skip:
            temp = sum(cardPoints[i:i+skip])
            max_points = max(max_points, total_points - temp)
            i += 1
        return max_points
        
    def maxScoreV2(self, cardPoints: List[int], k: int) -> int:
        # fast
        n = len(cardPoints)
        left, right = 0, n - k
        total_points = sum(cardPoints[right:])
        answer = total_points
        while right < n:
            total_points += (cardPoints[left] - cardPoints[right])
            answer = max(answer, total_points)
            left += 1
            right += 1
        return answer


if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/max_points_from_cards_testcase.txt", "r") as file:
        card_points = literal_eval(file.readline().strip())
        k = int(file.readline().strip())

    solution = Solution()

    start = time()
    max_point = solution.maxScoreV2(card_points, k)
    print(max_point)
    print(f"Time elapsed : {(time() - start) * 1000} miiliseconds")
    