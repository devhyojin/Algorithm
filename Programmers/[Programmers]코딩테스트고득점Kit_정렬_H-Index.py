# def solution(citations):
#     n = len(citations)
#     cit_cnt = [0 for _ in range(max(citations)+1)]
#     for cit in citations:
#         cit_cnt[cit]+= 1
#     for i in range(len(cit_cnt)-1,-1,-1):
#         if i <= n-sum(cit_cnt[:i]):
#             return i

def solution(citations):
    citations.sort(reverse=True)
    answer = list(enumerate(citations, start=1))
    return answer

print(solution([3, 0, 6, 1, 5]))