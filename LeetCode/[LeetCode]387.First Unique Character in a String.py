#sol1

class Solution:
    def firstUniqChar(self, s: str) -> int:

        visited = {}
        for i in s:
            if i not in visited:
                visited[i] = 1
            else:
                visited[i] += 1

        answer = -1
        for j in range(len(s)):
            if visited[s[j]] == 1:
                answer = j
                break

        return answer

```
리스트에 문자가 나올 때마다 나타난 횟수를 딕셔너리로 기록해서
단 한 번만 나온 문자를 구했다.
132ms 14.5MB
```
