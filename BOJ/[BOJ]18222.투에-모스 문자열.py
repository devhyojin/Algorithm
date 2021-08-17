#sol1
def changer(target, flag):
    if target < 3:
        if flag:
            print(w[target-1])
            return
        else:
            print(w[target-2])
            return
    else:
        #제일 큰 2의 제곱수의 지수
        x = len(bin(target))-3
        rest = target % (2**x)
        flag = not flag
        if rest:
            changer(rest, flag)
        else:
            changer(2**(x-1), flag)

k = int(input())
w = '01'
changer(k, True)

#sol2
k = int(input()) -1
flag = 0
while k:
    flag += k%2
    k//=2
print(flag%2)



