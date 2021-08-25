from collections import defaultdict


def solution(n, results):
    win_dic = defaultdict(set)  # key(승자), val(패자)
    lose_dic = defaultdict(set)  # key(패자), val(승자)
    for w, l in results:
        win_dic[w].add(l)
        lose_dic[l].add(w)

    for i in range(1, n + 1):
        # i에게 진 플레이어들은, i를 이긴 플레이어들에게도 졌음
        for loser in win_dic[i]:  # loser: i에게 진 플레이어들
            lose_dic[loser].update(lose_dic[i])  # lose_dic[i]: i를 이긴 플레이어들
        # i에게 이긴 플레이어들은, i에게 진 플레이어들에게도 이김
        for winner in lose_dic[i]:  # winner: i에게 이긴 플레이어들
            win_dic[winner].update(win_dic[i])  # win_dic[i]: i에게 진 플레이어들

    answer = 0
    for i in range(1, n + 1):
        if len(win_dic[i]) + len(lose_dic[i]) == n - 1:
            answer += 1
    return answer