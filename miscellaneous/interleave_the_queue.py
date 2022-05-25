from queue import Queue


def interLeaveQueue(q: Queue):
    # WRITE CODE HERE
    # stack1 = []

    # for _ in range(q.qsize() // 2):
    #     stack1.append(q.get())

    # # reverse queue
    # stack2 = []
    # for _ in range(q.qsize()):
    #     stack2.append(q.get())
    
    # # add queue
    # for pair in zip(stack1, stack2):
    #     q.put(pair[0])
    #     q.put(pair[1])

    # reverse queue
    stack = []
    for _ in range(q.qsize()):
        stack.append(q.get())
    
    for _ in range(len(stack) // 2):
        q.put(stack.pop())

    for _ in range(q.qsize()):
        q.put(q.get())
        q.put(stack.pop())

    for _ in range(q.qsize()):
        stack.append(q.get())
    
    for _ in range(len(stack)):
        q.put(stack.pop())


def print_queue(q):
    for i in range(q.qsize()):
        print(q.queue[0], end=" ")
        q.get()


if __name__ == '__main__':
    q = Queue()
    n = input()
    array = list(map(str, input().split()))
    for element in array:
        q.put(element)
    interLeaveQueue(q)
    print_queue(q)
