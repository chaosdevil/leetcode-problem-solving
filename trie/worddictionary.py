### sample trie data structure
import os

from ast import literal_eval

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.root = self.get_node()
        
    def get_node(self):
        return TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')
    
    def addWord(self, word: str) -> None:
        crawler = self.root
        length = len(word)
        for level in range(length):
            index = self.get_index(word[level])
            if not crawler.children[index]:
                crawler.children[index] = self.get_node()
            crawler = crawler.children[index]
        crawler.is_end = True

    def search(self, word: str) -> bool:
        crawler = self.root
        length = len(word)
        for i in range(length):
            if word[i] == '.':
                for sub_trie in crawler.children:
                    if sub_trie and self.search_deep(crawler, sub_trie, word[i+1:]):
                        return True
                return False
            if not crawler.children[self.get_index(word[i])]:
                return False
            crawler = crawler.children[self.get_index(word[i])]
        return crawler and crawler.is_end

    def search_deep(self, node, t, s):
        current = node
        for i in range(len(s)):
            if s[i] == '.':
                for sub_trie in current.children:
                    if sub_trie and self.search_deep(node, sub_trie, s[i+1:]):
                        return True
                return False
            if not current.children[self.get_index(s[i])]:
                return False
        return current != None and current.is_end
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
        

if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/worddictionary.txt", "r") as file:
        ops = literal_eval(file.readline().strip())
        words = literal_eval(file.readline().strip())
        
    result = []

    for i in range(len(ops)):
        if ops[i] == 'addWord':
            result.append(trie.addWord(words[i][0]))
        elif ops[i] == 'search':
            result.append(trie.search(words[i][0]))
        else:
            trie = WordDictionary()
        
    print(result)

