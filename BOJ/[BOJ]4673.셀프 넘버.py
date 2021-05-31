num_list = set(range(1, 10001))
self_num = [1]*10001

def d(n):
    n = n + sum(map(int, str(n)))
    return n

for i in num_list:
    res = d(i)
    if res < 10001:
        self_num[res] = 0
    if self_num[i] == 1:
        print(i)

