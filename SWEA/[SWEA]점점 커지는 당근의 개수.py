t = int(input())
for tc in range(1,t+1):
    n=int(input())
    carrots=list(map(int, input().split()))
    answer=[1]
    flag = False
    temp = 1
    for i in range(1,n):
        if carrots[i] == carrots[i-1]+1:
            temp += 1
        else:
            if temp > 1:
                answer.append(temp)
                temp = 1
    answer.append(temp)
    print(f'#{tc} {max(answer)}')