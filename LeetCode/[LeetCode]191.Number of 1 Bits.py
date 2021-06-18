# sol1
class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = bin(n).count('1')
        return answer
```
이진수로 변환 후, 1의 갯수를 세는 방식으로 풀었다.
24ms 14.3MB
```