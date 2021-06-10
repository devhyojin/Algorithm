from itertools import combinations
n, m = map(int, input().split())
cards = list(map(int, input().split()))
picked = list(combinations(cards, 3))
ans = 0
for picked in list(combinations(cards, 3)):
  temp_sum = sum(picked)
  if temp_sum <= m and temp_sum > ans:
    ans = temp_sum
print(ans)
