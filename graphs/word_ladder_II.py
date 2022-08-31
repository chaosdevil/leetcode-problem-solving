from ast import literal_eval
from collections import defaultdict
from typing import List
import os
import string


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]):
        alphabet = string.ascii_lowercase
        
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        if beginWord in word_set:
            word_set.remove(beginWord)
        
        # build an adjacency list
        queue = [beginWord]
        special_adj = defaultdict(list)
        special_adj[beginWord] = []
        visited = {beginWord:0}
        
        while queue:
            current = queue.pop(0)
            for i in range(len(current)):
                temp = current
                for j in range(len(alphabet)):
                    temp = temp[:i] + alphabet[j] + temp[i+1:]
                    if temp != current:
                        if temp in word_set:
                            # if it has not been visited
                            if visited.get(temp, 0) == 0:
                                visited[temp] = visited.get(current, 0) + 1
                                queue.append(temp)
                                special_adj[current].append(temp)
                            elif visited[temp] == visited[current] + 1:
                                special_adj[current].append(temp)
                                
        # perform depth-first search
        # print(special_adj)
        result = []
        res = []
        visited = set()
        self.dfs(beginWord, endWord, special_adj, result, visited, res)
        return result
        
    def dfs(self, start, stop, graph, result, visited, res):
        visited.add(start)
        res.append(start)
        if start == stop:
            result.append(res[:])
            return
        for neighbor in graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, stop, graph, result, visited, res)
                res.pop()
                visited.remove(neighbor)
                    

if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/word_ladder_testcase.txt", "r") as file:
        beginWord = file.readline().strip().replace("\"", "")
        endWord = file.readline().strip().replace("\"", "")
        wordList = literal_eval(file.readline().strip())

    solution = Solution()
    print(solution.findLadders(beginWord, endWord, wordList))