from sys import stdin

while True:
    answer = True
    sentence = stdin.readline().rstrip()
    stack = []
    if sentence == '.':
        break
    for s in sentence:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] =='(':
                stack.pop()
            else:
                answer = False
                break
        elif s == ']':
            if stack and stack[-1] =='[':
                stack.pop()
            else:
                answer = False
                break
    if not stack and answer:
        print("yes")
    else:
        print("no")

