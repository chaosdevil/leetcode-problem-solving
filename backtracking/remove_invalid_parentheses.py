# Python3 program to remove invalid parenthesis

# Method checks if character is parenthesis(open
# or closed)
def isParenthesis(c):
    return ((c == '(') or (c == ')'))

# method returns true if contains valid
# parenthesis


def isValidString(s):
    cnt = 0
    for i in range(len(s)):
        if (s[i] == '('):
            cnt += 1
        elif (s[i] == ')'):
            cnt -= 1
        if (cnt < 0):
            return False
    return (cnt == 0)

# method to remove invalid parenthesis


def removeInvalidParenthesis(s):
    if (len(s) == 0):
        return None

    # visit set to ignore already visited
    visit = set()

    # queue to maintain BFS
    q = []
    temp = 0
    level = False

    # pushing given as starting node into queue
    q.append(s)
    visit.add(s)

    while(len(q)):
        s = q[0]
        q.pop(0)
        if (isValidString(s)):
            print(s)

            # If answer is found, make level true
            # so that valid of only that level
            # are processed.
            level = True
        if (level):
            continue
        for i in range(len(s)):
            if (not isParenthesis(s[i])):
                continue

            # Removing parenthesis from s and
            # pushing into queue,if not visited already
            temp = s[0:i] + s[i + 1:]
            if temp not in visit:
                q.append(temp)
                visit.add(temp)


# Driver Code
expression = "()())()"
removeInvalidParenthesis(expression)
expression = "()v)"
removeInvalidParenthesis(expression)
