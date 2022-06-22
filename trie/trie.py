import os

from ast import literal_eval

class TrieNode:
    def __init__(self):
        self.children = [0] * 26
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        crawler = self.root
        length = len(key)
        for level in range(length):
            index = ord(key[level]) - ord('a')
            if not crawler.children[index]:
                crawler.children[index] = TrieNode()
            crawler = crawler.children[index]
        crawler.is_end = True

    def search(self, key):
        crawler = self.root
        length = len(key)
        for level in range(length):
            index = ord(key[level]) - ord('a')
            if not crawler.children[index]:
                return False
            crawler = crawler.children[index]
        return crawler.is_end


if __name__ == "__main__":
    with open(os.path.dirname(__file__) + "/trie_testcase.txt", "r") as file:
        texts = literal_eval(file.readline().strip())

    trie = Trie()
    
    for word in texts:
        trie.insert(word)
    
    print(trie.search("their"))
    print(trie.search("thaw"))
    print(trie.search("any"))
    print(trie.search("them"))