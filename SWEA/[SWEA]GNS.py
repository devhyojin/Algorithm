num_dic = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}

t=int(input())
for _ in range(t):
    tc, n = input().split()
    print(tc)
    nums=input().split()
    for num in nums:
        num_dic[num] +=1
    for alp, cnt in num_dic.items():
        for _ in range(cnt):
            print(alp, end=" ")
    print()