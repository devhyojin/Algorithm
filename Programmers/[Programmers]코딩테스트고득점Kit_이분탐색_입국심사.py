def solution(n, times):
    l,r = 1, max(times)*n
    while l < r:
        mid = (l+r)//2
        passed = sum([mid//time for time in times])
        if passed < n:
            l = mid + 1
        elif passed >= n:
            r = mid
    return l
