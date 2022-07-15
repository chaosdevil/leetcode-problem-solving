# https://leetcode.com/problems/course-schedule/

import os

from ast import literal_eval
from time import time
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build adjacency list
        adj_list = [[] for _ in range(numCourses)]
        for preq in prerequisites:
            adj_list[preq[0]].append(preq[1])
        
        visited = set()
        path = set()
        
        for c in range(numCourses):
            if self.detect_cycle(c, adj_list, path, visited):
                return False
        return True
        
    def detect_cycle(self, course, adj_list, path, visited):

        # technique : backtracking
        if course in path:
            return True
        if course in visited:
            return False
        
        path.add(course)
        for c in adj_list[course]:
            if self.detect_cycle(c, adj_list, path, visited):
                return True
        path.remove(course)
        visited.add(course)
        
        return False

if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/course_schedule_testcase.txt", "r") as file:
        numCourses = int(file.readline().strip())
        prerequisites = literal_eval(file.readline().strip())

    solution = Solution()

    start = time()
    print(solution.canFinish(numCourses, prerequisites))
    print(f"Time elapsed : {(time() - start) * 1000} milliseconds")