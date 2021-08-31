#sol1(해쉬)
from collections import defaultdict
def solution(clothes):
    clothes_dic = defaultdict(int)
    for item, category in clothes:
        clothes_dic[category] += 1
    answer = 1
    for cnt in clothes_dic.values():
        answer *= (cnt+1)
    return answer -1

#sol2
from collections import Counter
from functools import reduce
def solution(clothes):
    clothes_dic = Counter([category for item, category in clothes])
    answer = reduce(lambda x, y: x*(y+1), clothes_dic.values(), 1)
    return answer-1

# (a+1)*(b+1)*(c+1) = 1 + a+b+c + ab+bc+ca + abc 이므로 모두 입지 않는 경우만 빼주자!