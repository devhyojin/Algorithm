from sys import stdin
input = stdin.readline

def game(turn, s, e):
    if s > e: return 0
    if dp[s][e]: return dp[s][e]

    if turn:
        max_score = max(game(False, s+1, e)+cards[s], game(False, s, e-1)+cards[e])
        dp[s][e] = max_score
        return max_score

    else:
        min_score = min(game(True, s+1, e), game(True, s, e-1))
        dp[s][e] = min_score
        return min_score

t = int(input())
for _ in range(t):
    n = int(input())
    cards = list(map(int, input().split()))
    dp = list(list(0 for _ in range(n)) for _ in range(n))
    print(game(True, 0, n-1))
