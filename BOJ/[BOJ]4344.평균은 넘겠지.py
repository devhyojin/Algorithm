from sys import stdin
C = int(stdin.readline())

for i in range(C):
    info = list(map(int, stdin.readline().split()))
    ppl = info[0]
    scores = info[1:]
    mean = sum(scores) / ppl

    passed = 0
    for j in scores:
        if j > mean:
            passed += 1
    ans = '{:.3f}'.format(round((passed*100/ppl),3))

    print(f'{ans}%')