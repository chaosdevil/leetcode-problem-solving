def mirror_queue(n, texts):
    stack = []
    for text in texts:
        stack.append(text)
    texts.extend(texts[::-1])
    return texts


if __name__ == "__main__":
    n = int(input())
    texts = input().strip().split(" ")
    print(mirror_queue(n, texts))