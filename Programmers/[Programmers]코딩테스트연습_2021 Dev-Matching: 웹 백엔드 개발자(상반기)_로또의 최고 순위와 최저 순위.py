rank_dic = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}

def solution(lottos, win_nums):
    zero_cnt = lottos.count(0)
    dup_cnt = len(list(set(lottos)&set(win_nums)))
    return [rank_dic[dup_cnt+zero_cnt], rank_dic[dup_cnt]]