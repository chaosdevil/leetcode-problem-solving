import queue

counter = 0

class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
        global counter
        self._count = counter
        counter += 1

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self._count < other._count

def huffman_hidden():
    q = queue.PriorityQueue()

    for key in freq:
        q.put((freq[key], key, Node(freq[key], key)))

    while q.qsize() != 1:
        a = q.get()
        b = q.get()
        obj = Node(a[0] + b[0], '\0')
        obj.left = a[2]
        obj.right = b[2]
        q.put((obj.freq, obj.data, obj))

    root = q.get()
    root = root[2]

    return root

def dfs_hidden(obj, already):
    if not obj:
        return
    elif obj.data != '\0':
        code_hidden[obj.data] = already
    dfs_hidden(obj.right, already + '1')
    dfs_hidden(obj.left, already + '0')

# implement this function
def decode_huffman(root, s):
    decoded_s = ""
    length = len(s)
    current = root
    for i in range(length):
        # move to the left
        if s[i] == '0':
            current = current.left
        # move to the right
        elif s[i] == '1':
            current = current.right
        if current.data != "\x00":
            decoded_s += current.data
            current = root

    print(decoded_s)

# receive input
ip = input()
freq = {}

counter = 0

for ch in ip:
    if not freq.get(ch):
        freq[ch] = 1
    else:
        freq[ch] += 1

root = huffman_hidden()

code_hidden = {}

dfs_hidden(root, "")

if len(code_hidden) == 1:
    for key in code_hidden:
        code_hidden[key] = "0"

to_be_decoded = ""

for ch in ip:
    to_be_decoded += code_hidden[ch]

decode_huffman(root, to_be_decoded)


