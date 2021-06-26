from sys import stdin

n = int(stdin.readline())
stack, result, cnt, flag = [], [], 0, True

for _ in range(n):
    num = int(stdin.readline())
    while cnt < num:
        cnt += 1
        stack.append(cnt)
        result.append("+")
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        flag = False
        break
if flag:
    print("\n".join(result))
else:
    print("NO")



